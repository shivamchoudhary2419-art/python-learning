# Student Management API using Flask and SQLite

## Overview

This project is a Student Management System built using Python Flask and SQLite. It demonstrates database connectivity, API routing, and CRUD-related operations.

## Technologies Used

- Python
- Flask
- SQLite
- JSON
- VS Code

## Features

### 1. Home Route

URL:

/
Returns a welcome message.

### 2. View All Students

URL:

/students

Displays all student records from the database.

### 3. Search Student by Name

URL:

/student/<name>

Example:

/student/shivam

Returns the details of the specified student.

### 4. Update Student Marks

URL:

/update/<name>/<marks>

Example:

/update/shivam/99

Updates the marks of a student.

### 5. Add New Student

URL:

/add_student/<name>/<marks>/<course>

Example:

/add_student/anuj/95/CSE

Adds a new student to the database.

### 6. Total Students

URL:

/total_students

Returns the total number of students in the database.

## How to Run

1. Install Flask

pip install flask

2. Run the application

python app.py

3. Open browser and visit

http://127.0.0.1:5000/

## Project Structure

Day7/
│
├── app.py
├── students.db
├── .gitignore
└── README.md

## Author

Shivam Choudhary
