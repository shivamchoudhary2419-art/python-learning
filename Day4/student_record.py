import json 
import os

class Student:
    def __init__(self, name , marks , branch):
        self.name = name 
        self.marks = marks 
        self.branch = branch 

class studentmanager:
    def __init__(self):
        self.students = []
        
    def add_student(self, name , marks , branch):
        self.students.append({
            "name": name ,
            "marks" : marks,
            "branch": branch
        })
        print("student added successfully.")

    def view_student(self):
        if not self.students:
            print("No student found.")
            return
        
        print("\n Students Records")
        for student in self.students:
            print(
                f"Name: {student['name']},"
                f"Marks: {student['marks']},"
                f"Branch: {student['branch']},"
                
            )

    def search_student(self, name):
        for student in self.students:
            if student["name"].lower() == name.lower():
                print("\nStudent Found:")
                print(
                    f"Name: {student['name']}, "
                    f"Marks: {student['marks']}, "
                    f"Branch: {student['branch']}"
                )
                return

        print("Student not found.")

    def delete_student(self, name):
        for student in self.students:
            if student["name"].lower() == name.lower():
                self.students.remove(student)
                print("Student deleted successfully.")
                return

        print("Student not found.")

    def total_students(self):
        print(f"Total Students: {len(self.students)}")

    def save_students(self):
        print("Current students list:", self.students)
        print("Saving to:", os.path.abspath("students.json"))
        with open("students.json","w")as f:
            json.dump(self.students, f, indent=4)

        print("students saved successfully.")

    def load_students(self):
        try:
            with open("students.json","r")as f:
                self.students = json.load(f)

            print("Students loadede successfully.")
        except FileNotFoundError:
            print("No saved file found.")

manager = studentmanager()

while True:
    print("\n===== Student Record Manager =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Total Students")
    print("6. Save Students")
    print("7. Load Students")
    print("8. Exit")

    choice = input("Enter your choice:")
    if choice == "1":
        name = input("Enter name:") 
        marks = input("Enter marks:") 
        branch = input("Enter branch:") 

        manager.add_student(name, marks ,branch)

    elif choice == "2":
        manager.view_student()

    elif choice == "3":
        name = input("Enter student name to search: ")
        manager.search_student(name)

    elif choice == "4":
        name = input("Enter student name to delete: ")
        manager.delete_student(name)

    elif choice == "5":
        manager.total_students()

    elif choice == "6":
        manager.save_students()

    elif choice == "7":
        manager.load_students()

    elif choice == "8":
        print("Exiting Program...")
        break

    else:
        print("Invalid choice. Please try again.")
