# DevLog 📓
> A personal developer journal web app — built from scratch with Flask & SQLite.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.x-black?style=flat-square&logo=flask)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite)
![HTML/CSS](https://img.shields.io/badge/HTML%2FCSS-E34F26?style=flat-square&logo=html5)

---

## What is DevLog ?

DevLog is a full-stack web application I built to track my learning journey as a developer. It's a personal journal where you can create an account, write entries about what you're learning, edit them, and delete them.

I built this project entirely from scratch — from setting up the Python environment to deploying it on GitHub — to learn how backend web development actually works in practice.

---

## Features

- 🔐 **User authentication** — register, login, logout with secure password hashing
- 📝 **Full CRUD** — create, read, edit and delete journal entries
- 🛡️ **Route protection** — only authenticated users can create or modify posts
- 👤 **Ownership check** — users can only edit and delete their own posts
- 🎨 **Custom dark UI** — responsive interface built with pure HTML/CSS
- ⚠️ **Custom 404 page** — proper error handling for unknown routes
- 🔄 **Dynamic navbar** — shows username and logout when authenticated

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3 |
| Framework | Flask |
| Database | SQLite via SQLAlchemy |
| Auth | Flask-Login + Werkzeug |
| Frontend | HTML5, CSS3 (no framework) |
| Version Control | Git & GitHub |

---

## Project Structure

```
devlog/
├── app.py                  # App config, models, all routes
├── requirements.txt        # Python dependencies
├── static/
│   └── style.css           # Custom dark theme CSS
├── templates/
│   ├── base.html           # Base layout with dynamic navbar
│   ├── index.html          # Homepage — list of all posts
│   ├── register.html       # Registration form
│   ├── login.html          # Login form
│   ├── post_form.html      # Shared form for create & edit
│   ├── post_detail.html    # Single post view
│   └── 404.html            # Custom error page
└── instance/
    └── devlog.db           # SQLite database (auto-generated)
```

---

## Database Models

### User
| Column | Type | Description |
|---|---|---|
| id | Integer | Primary key |
| username | String(80) | Unique username |
| password | String(200) | Hashed password |

### Post
| Column | Type | Description |
|---|---|---|
| id | Integer | Primary key |
| title | String(100) | Entry title |
| content | Text | Entry content |
| date | DateTime | Auto-set on creation |
| user_id | Integer | Foreign key → User |

---

## How It Works

### Authentication
Passwords are never stored in plain text. When a user registers, the password is hashed using Werkzeug's `generate_password_hash`. On login, `check_password_hash` compares the input against the stored hash. Sessions are managed by Flask-Login.

### Route Protection
Routes like `/post/new`, `/post/<id>/edit` and `/post/<id>/delete` are decorated with `@login_required` — unauthenticated users are redirected to the login page automatically.

### Ownership Check
Even if a logged-in user tries to edit someone else's post directly via URL, the app checks `post.user_id != current_user.id` and redirects them to the homepage.

### Templates
All pages extend `base.html` using Jinja2's `{% extends %}` and `{% block content %}` system — meaning the navbar, CSS, and flash messages are defined once and reused everywhere.

---

## Installation & Setup

```bash
# 1. Clone the repo
git clone https://github.com/DZ3G/devlog.git
cd devlog

# 2. Create and activate virtual environment
python -m venv venv

# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

> The `instance/devlog.db` file is created automatically on first run.

---

## What I Learned Building This

- Setting up an isolated Python environment with `venv`
- Structuring a Flask application with routes, models and templates
- Designing relational database models with SQLAlchemy (one-to-many relationship between User and Post)
- Implementing secure user authentication from scratch (hashing, sessions, login protection)
- Using Jinja2 templating to build dynamic HTML pages
- Separating concerns between backend logic (`app.py`) and presentation (`templates/`, `static/`)
- Reading and interpreting HTTP logs in the terminal (`GET`, `POST`, `200`, `302`, `404`)
- Managing a project with Git — structured commits, `.gitignore`, `requirements.txt`

---

## Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Flask-Login Documentation](https://flask-login.readthedocs.io/)
- [roadmap.sh — Backend Path](https://roadmap.sh/backend)

## Author

**Mohammed Rafik Berrached**
Terminale STI2D SIN — Future étudiant Bac+3 Dev Web @ ESGI Paris (Sept. 2026)

[![GitHub](https://img.shields.io/badge/GitHub-DZ3G-181717?style=flat-square&logo=github)](https://github.com/DZ3G)
