
import sqlite3
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
app.secret_key = "super_secret_key"


# Database connection
def get_db_connection():
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    return conn


# Create database table
def init_db():
    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            dob TEXT NOT NULL,
            gender TEXT NOT NULL,
            course TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# Home
@app.route("/")
def home():
    return render_template("index.html")


# About
@app.route("/about")
def about():
    return render_template("about.html")


# Contact
@app.route("/contact")
def contact():
    return render_template("contact.html")


# Courses
@app.route("/courses")
def courses():
    return render_template("courses.html")


# Trainers
@app.route("/trainers")
def trainers():
    return render_template("trainers.html")


# Register
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        dob = request.form["dob"]
        gender = request.form["gender"]
        course = request.form["course"]

        conn = get_db_connection()

        # Check if user already exists
        existing_user = conn.execute(
            "SELECT * FROM users WHERE email = ?",
            (email,)
        ).fetchone()

        if existing_user:
            conn.close()
            return "User already exists with this email!"

        # Insert user into database
        conn.execute("""
            INSERT INTO users
            (name, email, password, dob, gender, course)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            name,
            email,
            password,
            dob,
            gender,
            course
        ))

        conn.commit()
        conn.close()

        return "Registration successful!"

    return render_template("register.html")


# Login
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        conn = get_db_connection()

        user = conn.execute(
            "SELECT * FROM users WHERE email = ?",
            (email,)
        ).fetchone()

        conn.close()

        if user and user["password"] == password:
            return "Login Successful!"

        return "Invalid Email or Password!"

    return render_template("login.html")


# API Register
@app.route("/api/register", methods=["POST"])
def api_register():

    data = request.get_json()

    if not data:
        return jsonify({
            "status": "error",
            "message": "Invalid JSON data"
        }), 400

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    dob = data.get("dob")
    gender = data.get("gender")
    course = data.get("course")

    # Check required fields
    if not all([name, email, password, dob, gender, course]):
        return jsonify({
            "status": "error",
            "message": "All fields are required"
        }), 400

    conn = get_db_connection()

    # Check if email already exists
    existing_user = conn.execute(
        "SELECT * FROM users WHERE email = ?",
        (email,)
    ).fetchone()

    if existing_user:
        conn.close()

        return jsonify({
            "status": "error",
            "message": "User already exists with this email"
        }), 400

    # Insert user
    conn.execute("""
        INSERT INTO users
        (name, email, password, dob, gender, course)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        name,
        email,
        password,
        dob,
        gender,
        course
    ))

    conn.commit()
    conn.close()

    return jsonify({
        "status": "success",
        "message": "Registration successful!"
    })


# API Login
@app.route("/api/login", methods=["POST"])
def api_login():

    data = request.get_json()

    if not data:
        return jsonify({
            "status": "error",
            "message": "Invalid JSON data"
        }), 400

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({
            "status": "error",
            "message": "Email and password are required"
        }), 400

    conn = get_db_connection()

    user = conn.execute(
        "SELECT * FROM users WHERE email = ?",
        (email,)
    ).fetchone()

    conn.close()

    if user and user["password"] == password:
        return jsonify({
            "status": "success",
            "message": "Login successful! Welcome back."
        })

    return jsonify({
        "status": "error",
        "message": "Invalid email or password!"
    }), 401


# Initialize database
init_db()


# Run Flask application
if __name__ == "__main__":
    app.run(debug=True)
