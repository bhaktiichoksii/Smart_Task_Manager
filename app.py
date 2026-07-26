from flask import Flask, render_template
from database.databse import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABSE_URL"] = "sqlite:///task_manager.db"
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

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)