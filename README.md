# Smart Task Manager 📋

A modern, responsive, full-stack Web Application built using **Python, Flask, SQLAlchemy, SQLite, HTML5, CSS3, JavaScript, and Jinja2 Templates**.

Designed as a professional **Admin Dashboard UI**.

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
  - [Authentication Flow](#authentication-flow)
  - [Task CRUD Flow](#task-crud-flow)
- [Screenshots & UI Showcase](#-screenshots--ui-showcase)
- [Future Enhancements](#-future-enhancements)
- [Author & License](#-author--license)

---

## 🚀 Project Overview

**Smart Task Manager** provides a simple, clean, and intuitive task management interface where registered users can record, monitor, update, and manage daily goals. The application enforces secure authentication, session management, and color-coded status badges for pending and completed tasks.

---

## ✨ Key Features

- **Responsive Dark Blue Navbar**: Branding logo, page links (Home, Dashboard, Login, Register, Profile, Logout), and active page highlighting.
- **Collapsible Sidebar**: Slide-in/out left sidebar toggling via hamburger icon, with user profile shortcut, task list section, and logout button.
- **Interactive Dashboard**:
  - **Summary Stat Cards**: Real-time counts for Total Tasks, Pending Tasks, Completed Tasks, and Completion Rate %.
  - **Modern Task Table**: Columns for Task Title, Description, Status (Orange badge for Pending, Green badge for Completed), Created Date, and Action buttons.
  - **Confirmation Dialogs**: Deletion confirmation prompt (`"Are you sure you want to delete this task?"`) before removing task records.
- **User Profile Page**: Detailed view displaying user name, email, avatar icon, and a task statistics breakdown grid.
- **Secure Authentication**: Password hashing using `werkzeug.security` (`generate_password_hash`, `check_password_hash`) and session-based route protection.
- **Show/Hide Password Toggle**: Eye icon button in Login and Register forms to toggle password text visibility.
- **Password Strength Indicator**: Real-time client-side password strength meter (Weak, Medium, Strong).
- **Single-Time Flash Alerts**: Auto-dismissing green, red, and yellow notification banners.

---

## 🛠️ Technology Stack

| Layer | Technology |
| :--- | :--- |
| **Backend Framework** | Python 3 (Flask Framework) |
| **Database ORM** | SQLAlchemy |
| **Database Engine** | SQLite 3 |
| **Templating Engine** | Jinja2 |
| **Frontend UI** | HTML5, Modern CSS3 (Flexbox & Grid), JavaScript (Vanilla JS) |
| **Typography & Icons**| Google Fonts (Inter), Font Awesome 6 |

---

## 📁 Folder Structure

```text
Smart_Task_Manager/
│
├── app.py                  # Main Flask Application Routes & Controller
├── config.py               # Configuration Settings
├── requirements.txt        # Python Dependencies List
├── README.md               # Project Documentation
│
├── database/
│   └── database.py         # SQLAlchemy Database Connection Instance
│
├── models/
│   ├── user.py             # User SQLAlchemy Database Model
│   └── task.py             # Task SQLAlchemy Database Model
│
├── static/
│   ├── css/
│   │   └── style.css       # Complete Custom CSS Design System
│   ├── js/
│   │   └── script.js      # Sidebar Toggle, Password Hide/Show, JS Validation
│   └── images/             # Static Images & Assets
│
├── templates/
│   ├── base.html           # Master Layout Template (Navbar, Flash Alerts, Footer)
│   ├── index.html          # Public Landing Home Page
│   ├── login.html          # Login Form Template
│   ├── register.html       # User Registration Template
│   ├── dashboard.html      # Admin Dashboard & Task Table
│   ├── profile.html        # User Profile & Stats View
│   ├── add_task.html       # Add Task Form Template
│   └── edit_task.html      # Edit Task Form Template
│
└── instance/
    └── task_manager.db     # SQLite Database File
```

---

## 🗄️ Database Schema

### 1. `User` Model (`models/user.py`)
- `id`: Integer (Primary Key, Auto-increment)
- `name`: String(100), Required
- `email`: String(100), Unique, Required
- `password`: String(255), Hashed, Required

### 2. `Task` Model (`models/task.py`)
- `id`: Integer (Primary Key, Auto-increment)
- `title`: String(200), Required
- `description`: Text
- `status`: String(20), Default: `"Pending"` (Options: `"Pending"`, `"Completed"`)
- `created_at`: DateTime, Default: `datetime.utcnow`
- `user_id`: Integer, Foreign Key -> `user.id`

---

## ⚙️ Installation & Setup Guide

### 1. Prerequisites
- Python 3.8 or higher installed on your system.
- Git installed.

### 2. Clone Repository or Open Project Folder
```bash
cd d:\Projects\Smart_Task_Manager
```

### 3. Create a Virtual Environment
```bash
# Windows
python -m venv .venv

# Activate Virtual Environment (Windows PowerShell)
.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run the Application

Execute `app.py` directly:
```bash
python app.py
```

Open your browser and navigate to:
```text
http://127.0.0.1:5000/
```

---

## 🔄 Project Workflow

### Authentication Flow
1. User visits `/register` -> Enters Name, Email, Password -> Password is hashed -> Record stored in SQLite -> Redirected to `/login`.
2. User enters credentials at `/login` -> Hash is checked -> User ID stored in `session["user_id"]` -> Access granted to `/dashboard`.
3. User clicks `/logout` -> Session cleared -> Flash message displayed -> Redirected to `/login`.

### Task CRUD Flow
- **Create**: Click "+ Add New Task" -> Fill Title, Description, Status -> Task saved to DB.
- **Read**: Dashboard fetches user's tasks -> Displays total counters, pending counts, completed counts, and task table.
- **Update**: Click "Edit" icon -> Pre-filled form loads -> Submit changes -> Task record updated.
- **Delete**: Click "Delete" icon -> Confirmation prompt -> Task record deleted.

---

## 🔮 Future Enhancements

- Due Date & Priority Tagging (High, Medium, Low).
- Search & Filter bar by Status or Title keyword.
- Export task history to PDF / CSV report.
- Dark mode toggle option.

---

## 👤 Author & License

- **Developer**: Bhakti Choksi
- **Degree**: MCA (Master of Computer Applications)
- **License**: MIT License