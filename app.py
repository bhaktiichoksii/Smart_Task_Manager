import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash, session
from database.database import db
from models.user import User
from models.task import Task
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize Flask App
app = Flask(__name__)

# Secret key for session management
app.secret_key = "my_secret_key"

# Database Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///task_manager.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize SQLAlchemy Database
db.init_app(app)

# Ensure instance folder and database tables exist
with app.app_context():
    os.makedirs("instance", exist_ok=True)
    db.create_all()

    # Self-healing check: Ensure created_at column exists in task table
    try:
        conn = sqlite3.connect("instance/task_manager.db")
        cursor = conn.cursor()
        cursor.execute("ALTER TABLE task ADD COLUMN created_at DATETIME;")
        conn.commit()
        conn.close()
    except Exception:
        pass


# Home Page Route
@app.route("/")
def home():
    return render_template("index.html")


# About Page Route
@app.route("/about")
def about():
    return redirect(url_for("home"))


# Contact Page Route
@app.route("/contact")
def contact():
    return redirect(url_for("home"))


# User Profile Page Route
@app.route("/profile")
def profile():
    user_id = session.get("user_id")
    if not user_id:
        flash("Please login first!", "error")
        return redirect(url_for("login"))

    user = User.query.get(user_id)
    tasks = Task.query.filter_by(user_id=user_id).all()

    total_tasks = len(tasks)
    pending_tasks = len([t for t in tasks if t.status == "Pending"])
    completed_tasks = len([t for t in tasks if t.status == "Completed"])

    return render_template(
        "profile.html",
        user=user,
        total_tasks=total_tasks,
        pending_tasks=pending_tasks,
        completed_tasks=completed_tasks
    )


# User Registration Route
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"].strip()
        email = request.form["email"].strip().lower()
        password = request.form["password"].strip()
        confirm_password = request.form["confirm_password"].strip()

        # Validate matching passwords
        if password != confirm_password:
            flash("Passwords do not match!", "error")
            return render_template("register.html")

        # Check if email is already registered (case-insensitive)
        existing_user = User.query.filter(db.func.lower(User.email) == email).first()
        if existing_user:
            flash("Email already registered. Please login with your password or use a new email.", "error")
            return redirect(url_for("login"))

        # Hash password and create new user record
        hashed_password = generate_password_hash(password)
        new_user = User(
            name=name,
            email=email,
            password=hashed_password
        )

        db.session.add(new_user)
        db.session.commit()

        flash(f"Welcome {name}! Your account has been created successfully. Please login.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")


# User Login Route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"].strip().lower()
        password = request.form["password"].strip()

        # Find user by email (case-insensitive)
        user = User.query.filter(db.func.lower(User.email) == email).first()

        if user:
            is_valid_password = False
            try:
                is_valid_password = check_password_hash(user.password, password)
            except Exception:
                is_valid_password = False

            # Fallback for plain-text passwords from legacy test database entries
            if not is_valid_password and user.password == password:
                is_valid_password = True
                user.password = generate_password_hash(password)
                db.session.commit()

            if is_valid_password:
                session["user_id"] = user.id
                flash("Login Successful!", "success")
                return redirect(url_for("dashboard"))
            else:
                flash("Incorrect Password!", "error")
        else:
            flash("User Not Found! Please register a new account.", "error")

    return render_template("login.html")


# Dashboard Route
@app.route("/dashboard")
def dashboard():
    user_id = session.get("user_id")
    if not user_id:
        flash("Please login first!", "error")
        return redirect(url_for("login"))

    user = User.query.get(user_id)
    tasks = Task.query.filter_by(user_id=user_id).all()

    return render_template(
        "dashboard.html",
        user=user,
        tasks=tasks
    )


# Add New Task Route
@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    if "user_id" not in session:
        flash("Please login first!", "error")
        return redirect(url_for("login"))

    if request.method == "POST":
        title = request.form["title"].strip()
        description = request.form["description"].strip()
        status = request.form["status"]

        new_task = Task(
            title=title,
            description=description,
            status=status,
            user_id=session["user_id"]
        )

        db.session.add(new_task)
        db.session.commit()

        flash("Task added successfully!", "success")
        return redirect(url_for("dashboard"))

    return render_template("add_task.html")


# Edit Task Route
@app.route("/edit_task/<int:id>", methods=["GET", "POST"])
def edit_task(id):
    if "user_id" not in session:
        flash("Please login first!", "error")
        return redirect(url_for("login"))

    task = Task.query.filter_by(
        id=id,
        user_id=session["user_id"]
    ).first_or_404()

    if request.method == "POST":
        task.title = request.form["title"].strip()
        task.description = request.form["description"].strip()
        task.status = request.form["status"]

        db.session.commit()

        flash("Task Updated Successfully!", "success")
        return redirect(url_for("dashboard"))

    return render_template(
        "edit_task.html",
        task=task
    )


# Delete Task Route
@app.route("/delete_task/<int:id>")
def delete_task(id):
    if "user_id" not in session:
        flash("Please login first!", "error")
        return redirect(url_for("login"))

    task = Task.query.get_or_404(id)

    if task.user_id != session["user_id"]:
        flash("Access Denied!", "error")
        return redirect(url_for("dashboard"))

    db.session.delete(task)
    db.session.commit()

    flash("Task Deleted Successfully!", "success")
    return redirect(url_for("dashboard"))


# Logout Route
@app.route("/logout")
def logout():
    session.pop("user_id", None)
    flash("Logged out successfully!", "success")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)