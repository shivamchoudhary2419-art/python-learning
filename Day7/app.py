from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

DB_PATH = r"C:\Users\chach\OneDrive\Desktop\AIINTERN\Day5\students.db"

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


# Home Route
@app.route("/")
def home():
    return "Welcome to Student API"


# Show All Students
@app.route("/students")
def students():

    conn = get_db_connection()

    students = conn.execute(
        "SELECT * FROM students"
    ).fetchall()

    conn.close()

    return jsonify([dict(student) for student in students])


# Search Student By Name
@app.route("/student/<name>")
def search_student(name):

    conn = get_db_connection()

    student = conn.execute(
        """
        SELECT * FROM students
        WHERE TRIM(LOWER(name)) = TRIM(LOWER(?))
        """,
        (name,)
    ).fetchone()

    conn.close()

    if student:
        return jsonify(dict(student))

    return jsonify({
        "message": "Student not found"
    })


# Update Marks
@app.route("/update/<name>/<int:marks>")
def update_marks(name, marks):

    conn = get_db_connection()

    conn.execute(
        """
        UPDATE students
        SET age = ?
        WHERE TRIM(LOWER(name)) = TRIM(LOWER(?))
        """,
        (marks, name)
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": f"{name} updated successfully",
        "new_marks": marks
    })


# Add Student
@app.route("/add_student/<name>/<int:marks>/<course>")
def add_student(name, marks, course):

    conn = get_db_connection()

    conn.execute(
        """
        INSERT INTO students(name, age, grade)
        VALUES (?, ?, ?)
        """,
        (name, marks, course)
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message": f"{name} added successfully",
        "marks": marks,
        "course": course
    })


# Total Students
@app.route("/total_students")
def total_students():

    conn = get_db_connection()

    total = conn.execute(
        "SELECT COUNT(*) FROM students"
    ).fetchone()[0]

    conn.close()

    return jsonify({
        "total_students": total
    })


if __name__ == "__main__":
    app.run(debug=True)