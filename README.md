# TurtleArt Studio

A full-stack Python Turtle pattern learning website with account login, a 100-pattern library, animated browser previews, downloadable Turtle scripts, favorites, history, and an optional AI code-generation lab.

## Features
- Signup/login with securely hashed passwords (Werkzeug)
- Personalized dashboard showing the logged-in user's name
- 100 patterns across 10 categories and three difficulty levels
- Search and category/difficulty filters
- Animated drawing studio with play, pause, restart and speed controls
- Python Turtle source code for every pattern
- Copy code and download standalone `.py` files
- Favorites and recently viewed history
- Optional AI Turtle code generation (requires your own API key)

## Run on Windows 11 (PowerShell)
Open PowerShell in this project folder:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000 in your browser and create an account.

If PowerShell blocks activation, run:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## Run a downloaded Turtle pattern
Install Python 3, download a `.py` file from the studio and run:
```powershell
python p001_turtle_art.py
```
Python Turtle opens a separate desktop drawing window. It is not executed inside the website.

## Enable optional AI generation
1. Install the optional SDK: `pip install openai`
2. Set your API key in the server environment (never in browser JavaScript):
```powershell
$env:OPENAI_API_KEY="your-api-key"
$env:OPENAI_MODEL="gpt-4.1-mini"
python app.py
```
AI usage may incur API charges. The ready-made 100-pattern library works without an API key.

## Production checklist
- Set a strong random `SECRET_KEY` in the hosting environment.
- Use HTTPS and a production WSGI server (for example, Gunicorn).
- Configure persistent storage for `instance/turtleart.db`.
- Add CSRF protection, email verification, password reset, rate limiting and backups before public production use.
- Review AI-generated code before running it.

## Tech stack
Python, Flask, SQLite, HTML, CSS, JavaScript Canvas, Python Turtle.
