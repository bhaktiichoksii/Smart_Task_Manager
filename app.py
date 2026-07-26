from flask import Flask, render_template, request, redirect, url_for, flash
from database.database import db
from models.user import User
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.secret_key = "my_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///task_manager.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

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

        # Find user
        user = User.query.filter_by(email=email).first()

        # User not found
        if not user:
            flash("User not found. Please register first.", "error")
            return render_template("login.html")

        # Check password
        if check_password_hash(user.password, password):
            flash(f"Welcome {user.name}! Login Successful.", "success")
            return redirect(url_for("home"))
        else:
            flash("Incorrect password.", "error")
            return render_template("login.html")

    return render_template("login.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)