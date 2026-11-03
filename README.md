# 🐢 TurtleArt Studio

### Create • Explore • Animate • Learn Python Turtle Graphics

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask-Web%20Framework-black?style=for-the-badge&logo=flask" />
  <img src="https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" />
  <img src="https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite" />
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" />
</p>

---

## 🌟 About the Project

**TurtleArt Studio** is an interactive web application designed to make Python Turtle Graphics more creative, accessible, and enjoyable.

It allows users to explore 100+ creative drawing patterns, watch animated drawing previews, understand the Python code behind each design, and download ready-to-run Python Turtle scripts.

Whether you are a beginner learning Python or a developer exploring creative programming, TurtleArt Studio provides a simple environment to learn through visual experiences.

### 💡 Our Vision

Make programming more interesting by transforming Python code into beautiful visual artwork.

---

## ✨ Key Features

### 🎨 1. Explore 100+ Turtle Patterns

* 100+ predefined drawing patterns.
* Multiple creative categories.
* Search and filter patterns.
* Explore different geometric and artistic designs.

### 🎬 2. Interactive Drawing Studio

* Watch patterns being drawn through animations.
* Play, pause, and restart animations.
* Adjust drawing speed.
* Experience designs through an interactive canvas.

### 💻 3. Python Code Viewer

* View the Python Turtle source code.
* Understand how each design is created.
* Copy code directly.
* Download standalone `.py` files.
* Run downloaded scripts using Python.

### 👤 4. User Authentication

* User registration and login.
* Secure password hashing.
* Personalized dashboard.
* User-specific favorites and history.

### ⭐ 5. Favorites & History

* Save your favorite patterns.
* Access previously viewed patterns.
* Keep your creative collection organized.

### 🤖 6. AI Pattern Generator

* Optional AI-powered pattern generation.
* Generate creative pattern ideas using an AI provider.
* Requires an appropriately configured API key.
* AI functionality is optional; the core application works without it.

---

## 🛠️ Technology Stack

| Technology    | Purpose                             |
| ------------- | ----------------------------------- |
| Python        | Backend programming                 |
| Flask         | Web application framework           |
| SQLite        | Database                            |
| HTML5         | Webpage structure                   |
| CSS3          | Responsive UI and styling           |
| JavaScript    | Interactive functionality           |
| Canvas API    | Animated pattern previews           |
| Python Turtle | Actual downloadable drawing scripts |
| Werkzeug      | Password hashing                    |

---

## 📂 Project Structure

```text
TurtleArt-Studio/
│
├── app.py
├── requirements.txt
├── README.md
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   ├── main.js
│   │   └── draw.js
│   │
│   └── images/
│
├── templates/
│   ├── landing.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   └── studio.html
│
└── patterns/
```

*The exact files and folders may vary slightly depending on the project version.*

---

## 🚀 Installation & Setup

Follow these instructions to run TurtleArt Studio locally.

### Prerequisites

Install the following:

* Python 3.10 or newer
* Visual Studio Code
* Git (optional)
* A modern web browser

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/TurtleArt-Studio.git
```

Navigate into the project:

```bash
cd TurtleArt-Studio
```

### Step 2: Create a Virtual Environment

**Windows PowerShell:**

```powershell
py -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

If activation is blocked:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate again.

### Step 3: Install Dependencies

```bash
python -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

### Step 4: Start the Application

```bash
python app.py
```

### Step 5: Open in Your Browser

Visit:

```text
http://127.0.0.1:5000
```

🎉 Congratulations! TurtleArt Studio is now running locally.

---

## 🖥️ How to Use

1. Open TurtleArt Studio in your browser.
2. Create a new account.
3. Log in to your dashboard.
4. Explore the available drawing patterns.
5. Select any pattern.
6. Watch its animated drawing preview.
7. View the corresponding Python code.
8. Copy or download the code.
9. Run the downloaded `.py` file using Python.

---

## 🐍 Running Downloaded Turtle Scripts

Python Turtle uses the Tkinter graphical interface.

After downloading a Python pattern:

```bash
python pattern.py
```

A separate Turtle graphics window should open and display the drawing.

**Note:** The website uses JavaScript Canvas for browser previews because Python Turtle's Tkinter window does not run directly inside a normal browser page.

---

## 🔐 Security & Privacy

The project includes:

* Password hashing using Werkzeug.
* Session-based authentication.
* SQLite database storage.

For a public production deployment, additional security measures are recommended:

* CSRF protection.
* Login rate limiting.
* Secure session configuration.
* Environment-based secret management.
* Email verification and password recovery.
* HTTPS configuration.

Never upload passwords, secret keys, or API credentials to GitHub.

---

## 🔮 Future Improvements

The following features can make TurtleArt Studio even more powerful:

* [ ] 500+ unique Turtle Graphics patterns.
* [ ] Advanced AI drawing generation.
* [ ] User-created pattern uploads.
* [ ] Live Python code editor.
* [ ] Custom color palettes.
* [ ] Export drawings as PNG and SVG.
* [ ] Download animations as GIF.
* [ ] Community pattern sharing.
* [ ] User profile customization.
* [ ] Leaderboard and achievements.
* [ ] Mobile-friendly drawing experience.
* [ ] Cloud deployment.

---

## 🎯 Learning Outcomes

This project demonstrates practical knowledge of:

* Python application development.
* Flask web development.
* Frontend and backend integration.
* Database management.
* User authentication.
* JavaScript Canvas animations.
* Python Turtle Graphics.
* API integration.
* Responsive web design.
* Project architecture and documentation.

---

## 🤝 Contributing

Contributions are welcome!

If you want to improve TurtleArt Studio:

1. Fork the repository.
2. Create a new feature branch.
3. Make your changes.
4. Test your implementation.
5. Submit a Pull Request.

---

## 👨‍💻 Developer

**Vansh Bakshi**

Full Stack Developer | Python Programmer | Flutter Developer | AI/ML Enthusiast

GitHub: [@VanshBakshi](https://github.com/VanshBakshi)

---

## ⭐ Support the Project

If you like TurtleArt Studio:

* Give the repository a ⭐ Star.
* Fork the project.
* Share it with other developers.
* Contribute new drawing patterns.

Every contribution helps make creative programming more accessible!

---

<p align="center">
  <b>Made with ❤️ and Python</b>
  <br>
  <i>Keep Creating. Keep Exploring. Keep Coding.</i>
</p>
