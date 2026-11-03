import os, json, sqlite3, secrets
from functools import wraps
from pathlib import Path
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify, send_file
from werkzeug.security import generate_password_hash, check_password_hash

BASE = Path(__file__).resolve().parent
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "change-this-secret-before-deploying-" + secrets.token_hex(8))
DB_PATH = BASE / "instance" / "turtleart.db"
PATTERNS = json.loads((BASE / "patterns.json").read_text(encoding="utf-8"))

def db():
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    return con

def init_db():
    DB_PATH.parent.mkdir(exist_ok=True)
    with db() as con:
        con.executescript("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        CREATE TABLE IF NOT EXISTS favorites (
            user_id INTEGER NOT NULL, pattern_id TEXT NOT NULL,
            PRIMARY KEY(user_id, pattern_id),
            FOREIGN KEY(user_id) REFERENCES users(id)
        );
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL, pattern_id TEXT NOT NULL,
            viewed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)

def login_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))
        return fn(*args, **kwargs)
    return wrapper

def current_user():
    if "user_id" not in session:
        return None
    with db() as con:
        return con.execute("SELECT id,name,email FROM users WHERE id=?", (session["user_id"],)).fetchone()

@app.context_processor
def inject_user():
    return {"logged_user": current_user()}

@app.route("/")
def index():
    if "user_id" in session:
        return redirect(url_for("dashboard"))
    return render_template("landing.html", total=len(PATTERNS))

@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method == "POST":
        name = request.form.get("name","").strip()
        email = request.form.get("email","").strip().lower()
        password = request.form.get("password","")
        if len(name) < 2 or "@" not in email or len(password) < 8:
            flash("Enter a valid name and email. Password must be at least 8 characters.", "error")
            return render_template("auth.html", mode="signup")
        try:
            with db() as con:
                cur = con.execute("INSERT INTO users(name,email,password_hash) VALUES(?,?,?)",
                                  (name,email,generate_password_hash(password)))
                session["user_id"] = cur.lastrowid
            flash("Your account is ready. Welcome!", "success")
            return redirect(url_for("dashboard"))
        except sqlite3.IntegrityError:
            flash("An account with this email already exists.", "error")
    return render_template("auth.html", mode="signup")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        email=request.form.get("email","").strip().lower()
        password=request.form.get("password","")
        with db() as con:
            user=con.execute("SELECT * FROM users WHERE email=?", (email,)).fetchone()
        if user and check_password_hash(user["password_hash"], password):
            session.clear()
            session["user_id"]=user["id"]
            return redirect(url_for("dashboard"))
        flash("Email or password is incorrect.", "error")
    return render_template("auth.html", mode="login")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

@app.route("/dashboard")
@login_required
def dashboard():
    user=current_user()
    with db() as con:
        fav_count=con.execute("SELECT COUNT(*) FROM favorites WHERE user_id=?", (user["id"],)).fetchone()[0]
        history_count=con.execute("SELECT COUNT(DISTINCT pattern_id) FROM history WHERE user_id=?", (user["id"],)).fetchone()[0]
        recent=con.execute("SELECT pattern_id FROM history WHERE user_id=? GROUP BY pattern_id ORDER BY MAX(viewed_at) DESC LIMIT 4",(user["id"],)).fetchall()
    recent_ids=[r["pattern_id"] for r in recent]
    recent_patterns=[p for pid in recent_ids for p in PATTERNS if p["id"]==pid]
    return render_template("dashboard.html", total=len(PATTERNS), fav_count=fav_count,
                           history_count=history_count, recent=recent_patterns)

@app.route("/patterns")
@login_required
def patterns_page():
    category=request.args.get("category","all")
    search=request.args.get("q","").strip().lower()
    difficulty=request.args.get("difficulty","all")
    items=PATTERNS
    if category!="all": items=[p for p in items if p["category_slug"]==category]
    if difficulty!="all": items=[p for p in items if p["difficulty"].lower()==difficulty]
    if search: items=[p for p in items if search in p["name"].lower() or search in p["category"].lower()]
    return render_template("patterns.html", patterns=items, categories=categories_list(), selected=category, q=request.args.get("q",""), difficulty=difficulty)

def categories_list():
    return [{"name":n,"slug":s} for n,s,_ in [
        ("Geometric Art","geometric",[]),("Spiral Art","spiral",[]),("Flower Designs","flowers",[]),
        ("Mandala Art","mandala",[]),("Mathematical Art","math",[]),("Fractal Art","fractals",[]),
        ("Nature Designs","nature",[]),("Abstract Art","abstract",[]),("Festival Designs","festivals",[]),
        ("Advanced Creative Art","advanced",[])]]

@app.route("/studio/<pattern_id>")
@login_required
def studio(pattern_id):
    pat=next((p for p in PATTERNS if p["id"]==pattern_id),None)
    if not pat: return "Pattern not found",404
    with db() as con:
        con.execute("INSERT INTO history(user_id,pattern_id) VALUES(?,?)",(session["user_id"],pattern_id))
        fav=con.execute("SELECT 1 FROM favorites WHERE user_id=? AND pattern_id=?",(session["user_id"],pattern_id)).fetchone()
    code_path=BASE/"patterns"/f"{pattern_id}.py"
    code=code_path.read_text(encoding="utf-8")
    return render_template("studio.html", pattern=pat, code=code, is_favorite=bool(fav))

@app.route("/download/<pattern_id>")
@login_required
def download(pattern_id):
    if not any(p["id"]==pattern_id for p in PATTERNS): return "Pattern not found",404
    return send_file(BASE/"patterns"/f"{pattern_id}.py", as_attachment=True, download_name=f"{pattern_id}_turtle_art.py")

@app.post("/favorite/<pattern_id>")
@login_required
def favorite(pattern_id):
    if not any(p["id"]==pattern_id for p in PATTERNS): return jsonify(ok=False),404
    with db() as con:
        exists=con.execute("SELECT 1 FROM favorites WHERE user_id=? AND pattern_id=?",(session["user_id"],pattern_id)).fetchone()
        if exists:
            con.execute("DELETE FROM favorites WHERE user_id=? AND pattern_id=?",(session["user_id"],pattern_id))
            saved=False
        else:
            con.execute("INSERT INTO favorites(user_id,pattern_id) VALUES(?,?)",(session["user_id"],pattern_id))
            saved=True
    return jsonify(ok=True,saved=saved)

@app.route("/favorites")
@login_required
def favorites():
    with db() as con:
        ids=[r["pattern_id"] for r in con.execute("SELECT pattern_id FROM favorites WHERE user_id=? ORDER BY rowid DESC",(session["user_id"],))]
    items=[p for p in PATTERNS if p["id"] in ids]
    return render_template("patterns.html", patterns=items, categories=categories_list(), selected="all", q="", difficulty="all", page_title="My Favorites")

@app.route("/api/patterns")
@login_required
def api_patterns():
    return jsonify(PATTERNS)

@app.route("/ai-generate", methods=["GET","POST"])
@login_required
def ai_generate():
    if request.method=="POST":
        prompt=request.form.get("prompt","").strip()
        # Optional AI integration: set OPENAI_API_KEY and install openai.
        api_key=os.getenv("OPENAI_API_KEY")
        if not prompt:
            flash("Describe the design you want first.", "error")
        elif not api_key:
            flash("AI mode is optional and is not configured yet. Add OPENAI_API_KEY to your environment to enable it. You can still explore all 100 ready-made patterns.", "error")
        else:
            try:
                from openai import OpenAI
                client=OpenAI(api_key=api_key)
                response=client.responses.create(
                    model=os.getenv("OPENAI_MODEL","gpt-4.1-mini"),
                    input="Write a complete, safe Python Turtle script for this design request. Use only turtle, math and colorsys. Return only Python code. User request: "+prompt
                )
                generated=response.output_text
                session["generated_code"]=generated
                session["generated_prompt"]=prompt
                return redirect(url_for("ai_result"))
            except Exception as e:
                flash("AI generation failed. Check your API key, model and internet connection.", "error")
    return render_template("ai.html")

@app.route("/ai-result")
@login_required
def ai_result():
    return render_template("ai_result.html", code=session.get("generated_code",""), prompt=session.get("generated_prompt",""))

@app.route("/profile")
@login_required
def profile():
    return render_template("profile.html", user=current_user())

@app.errorhandler(413)
def too_large(e): return "File too large",413

init_db()
if __name__=="__main__":
    app.run(debug=True)
