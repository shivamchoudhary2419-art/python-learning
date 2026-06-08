# Flask app routing
from flask import Flask, render_template, request,jsonify
import sqlite3
import os

app = Flask(__name__)
print("Database path:", os.path.abspath("students.db"))

def get_db_connection():
    conn = sqlite3.connect(
        r"C:\Users\chach\OneDrive\Desktop\AIINTERN\Day5\students.db"
    )
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    return "Welcome to Student API."
@app.route("/students")
def students():

    conn = get_db_connection()
    students = conn.execute(
        "SELECT * FROM students"
    ).fetchall()

    conn.close()

    return jsonify([dict(student) for student in students])

@app.route("/student/<name>")
def search_student(name):
    conn = get_db_connection()

    students = conn.execute(
        "SELECT * FROM students"
    ).fetchall()

    print("All Students:", [dict(s) for s in students])
    student = conn.execute(
        "SELECT * FROM students WHERE TRIM(LOWER(name))=TRIM(LOWER(?))",
        (name,)
    ).fetchone()


    conn.close()

    if student:
        return jsonify(dict(student))
    return jsonify(
        {"message": "Student not found"}
    )
@app.route("/topper")
def topper():

    conn = get_db_connection()

    student = conn.execute(
        "SELECT * FROM students ORDER BY grade ASC LIMIT 1"
    ).fetchone()

    conn.close()
    if student:
        return jsonify(dict(student))
    return jsonify({"message": "No student found."})

if __name__ == "__main__":
    app.run(debug=True)
