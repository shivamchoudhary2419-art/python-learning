students = [
    {"name": "Alice", "age": 20, "grade": "A"},
    {"name": "Bob", "age": 22, "grade": "B"},   
    {"name": "Charlie", "age": 21, "grade": "A"},
    {"name": "David", "age": 23, "grade": "C"},
]

def add_student(name,age,grade):
    student = {
        "name": name,
        "age": age,
        "grade": grade
    }
    students.append(student)

def view_students():
    for student in students:
        print(f"Name : {student['name']}, Age : {student['age']}, Grade : {student['grade']}")

def search_student(name):
    for student in students:
        if student['name'].lower() == name.lower():
            print(f"name : {student['name']}, age : {student['age']}, grade : {student['grade']}")
            return
    print("Student not found")

def delete_students(name):
    for student in students :
        if student["name"].lower() == name.lower():
            students.remove(student)
            print("Student Deleted")
            return 
    print("Student not found")

import os
file_path = os.path.join(os.path.dirname(__file__), "students.txt")
def save_students():
    with open(file_path, 'w') as f:
        for student in students:
            f.write(f"{student['name']},{student['age']},{student['grade']}\n")
            print("Students saved successfully.")
def load_students():
    students.clear()
    with open(file_path, "r")as f:
        for line in f:
            name , age , grade = line.strip().split(",")
            students.append({
                "name": name,
                "age": int(age),
                "grade": grade
            })
    print("Students loaded successfully.")

while True:
    print("\n===== Student Record Management System =====")
    print("1. Add student")
    print("2. View students")
    print("3. Search student")
    print("4. Delete student")
    print("5. Save students")
    print("6. Load students")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        grade = input("Enter student grade: ")
        add_student(name, age, grade)

    elif choice == "2":
        view_students()
    elif choice == "3":
        name = input("Enter student name to search: ")
        search_student(name)
    elif choice == "4":
        name = input("Enter student name to delete: ")
        delete_students(name)
    elif choice == "5":
        save_students()
    elif choice == "6":
        load_students()
    elif choice == "7":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
