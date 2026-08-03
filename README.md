# Smart Task Manager 📋

A simple Task Management Web Application developed using **Python, Flask, SQLAlchemy, SQLite, HTML5, CSS3, JavaScript, and Jinja2 Templates**.

This project was developed as part of my MCA learning to understand Flask, user authentication, database connectivity, and CRUD operations.

---

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Key Features](#-key-features)
- [Technology Stack](#-technology-stack)
- [Folder Structure](#-folder-structure)
- [Database Schema](#-database-schema)
- [Installation & Setup Guide](#-installation--setup-guide)
- [How to Run the Application](#-how-to-run-the-application)
- [Project Workflow](#-project-workflow)
- [Future Enhancements](#-future-enhancements)
- [Author & License](#-author--license)

---

# 🚀 Project Overview

Smart Task Manager is a web application where users can manage their daily tasks.

A registered user can create an account, log in securely, and perform basic task management operations such as adding, viewing, editing, and deleting tasks.

The main purpose of this project is to learn Flask development, database integration, authentication, session management, and CRUD operations.

---

# ✨ Key Features

- User Registration
- Secure User Login
- Password Hashing using Werkzeug
- Session Management
- Dashboard for Logged-in Users
- Add New Task
- View All Tasks
- Edit Existing Task
- Delete Task
- Flash Messages for Success and Error
- Responsive Navigation Bar
- Sidebar Navigation
- SQLite Database Integration

---

# 🛠️ Technology Stack

| Layer | Technology |
| :--- | :--- |
| Backend | Python, Flask |
| Database | SQLite |
| ORM | SQLAlchemy |
| Frontend | HTML5, CSS3, JavaScript |
| Template Engine | Jinja2 |
| Version Control | Git & GitHub |
| Deployment | Render |

---

# 📁 Folder Structure

```text
Smart_Task_Manager/
│
├── app.py                  # Main Flask Application
├── requirements.txt        # Project Dependencies
├── Procfile               # Render Deployment File
├── README.md              # Project Documentation
│
├── database/
│   └── database.py        # Database Configuration
│
├── models/
│   ├── user.py            # User Model
│   └── task.py            # Task Model
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── add_task.html
│   ├── edit_task.html
│   └── profile.html
│
└── instance/
    └── task_manager.db
```

---

# 🗄️ Database Schema

## User Table

| Field | Description |
|-------|-------------|
| id | Primary Key |
| name | User Name |
| email | User Email |
| password | Hashed Password |

---

## Task Table

| Field | Description |
|-------|-------------|
| id | Primary Key |
| title | Task Title |
| description | Task Description |
| status | Pending / Completed |
| user_id | Linked User ID |

---

# ⚙️ Installation & Setup Guide

## Prerequisites

- Python 3.8 or above
- Git
- VS Code (Recommended)

## Clone Repository

```bash
git clone https://github.com/bhaktiichoksii/Smart_Task_Manager.git
```

## Open Project

```bash
cd Smart_Task_Manager
```

## Create Virtual Environment

```bash
python -m venv .venv
```

## Activate Virtual Environment

```bash
.venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🚀 How to Run the Application

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

---

# 🔄 Project Workflow

## User Registration

- User enters Name, Email and Password.
- Password is converted into a hashed password.
- User information is stored in SQLite database.

---

## User Login

- User enters Email and Password.
- Password is verified.
- Session is created after successful login.
- User is redirected to Dashboard.

---

## Task Management

The logged-in user can:

- Add New Task
- View All Tasks
- Edit Existing Task
- Delete Task
- Logout

Each user can only manage their own tasks.

---

# 🔮 Future Enhancements

Some features that can be added in future:

- Task Priority
- Due Date
- Search Tasks
- Filter Tasks
- User Profile Update
- Change Password
- Forgot Password
- PostgreSQL Database
- Email Verification

---

# 👤 Author & License

**Developer:** Bhakti Choksi

**Course:** Master of Computer Applications (MCA)

**Project Type:** Academic Learning Project

**GitHub Repository:**
https://github.com/bhaktiichoksii/Smart_Task_Manager

**Live Project:**
https://smart-task-manager-7tmj.onrender.com

**License:** This project is created for learning and educational purposes.