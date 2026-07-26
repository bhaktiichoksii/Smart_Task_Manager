from flask import Flask, render_template, request, redirect, url_for, flash, session
from database.database import db
from models.user import User
from models.task import Task
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.secret_key = "my_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///task_manager.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
import os

with app.app_context():
    print("Database Path:")
    print(os.path.abspath("instance/task_manager.db"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return "📖About Page"

@app.route("/contact")
def contact():
    return "📞Contact Page"

@app.route("/profile")
def profile():
    return "👤Profile"

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        hashed_password = generate_password_hash(password)
        confirm_password = request.form["confirm_password"]

        if password != confirm_password:
            flash("Passwords do not match!", "error")
            return render_template("register.html")

        # Check if email already exists
        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            flash("Email already registered. Please login.", "error")
            return redirect(url_for("login"))
        
        # Create User object
        new_user = User(
            name=name,
            email=email,
            password=hashed_password
        )

        # Save to database
        db.session.add(new_user)
        db.session.commit()

        # Success message
        flash(
            f"Welcome {name}! Your account has been created successfully.",
            "success"
        )

        # Go to Login Page
        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        print("=" * 40)
        print("Entered Email :", email)
        print("Entered Password :", password)

        user = User.query.filter_by(email=email).first()

        print("\n===== ALL USERS IN DATABASE =====")

        users = User.query.all()

        for u in users:
            print(u.id, u.name, u.email)

        print("===============================\n")

        if user:
            print("User Found:", user.email)
        else:
            print("No user found with email:", email)

        if user:
            print("Password in DB :", user.password)

            result = check_password_hash(user.password, password)

            print("Password Match :", result)

            if result:
                session["user_id"] = user.id
                flash("Login Successful!", "success")
                return redirect(url_for("dashboard"))
            else:
                flash("Incorrect Password!", "error")
        else:
            flash("User Not Found!", "error")

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():

    user_id = session.get("user_id")

    if not user_id:
        flash("Please login first!", "error")

        return redirect(url_for("login"))

    user = User.query.get(user_id)

    return render_template("dashboard.html", user=user)

@app.route("/add_task", methods=["GET", "POST"])
def add_task():

    if "user_id" not in session:
        flash("Please login first!", "error")
        return redirect(url_for("login"))

    if request.method == "POST":

        title = request.form["title"]
        description = request.form["description"]
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

@app.route("/logout")
def logout():

    session.pop("user_id", None)

    flash("Logged out successfully!", "success")

    return redirect(url_for("login"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)