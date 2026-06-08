import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()
# Table creation

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        age INTEGER,
        grade TEXT
        )'''
)

conn.commit()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print(cursor.fetchall())

print("Table Created Successfully.")

def add_student():
    name = input("Enter name: ")
    age = input("Enter age: ")
    grade = input("Enter grade: ")
    try:
        cursor.execute('INSERT INTO students (name, age, grade) VALUES (?, ?, ?)', (name, age , grade))
        conn.commit()
        print(f"Student {name} Added Successfully.")
    except sqlite3.IntegrityError:
        print(f"\n❌ Student '{name}' already exists.\n")

def view_student():
     cursor.execute("SELECT * FROM students") 
     rows = cursor.fetchall() 
     if not rows: 
        print("\n⚠ No students found.\n") 
        return 
     print("\n===== STUDENT RECORDS =====") 
     print("ID\tName\tAge\tGrade") 
     print("-" * 30) 
     for row in rows: 
         print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}") 
     print()

def update_student():
    student_id = int(input("Enter student ID to Update: "))
    cursor.execute(
       "SELECT * FROM students WHERE id=?",
       (student_id,)
    )  

    student = cursor.fetchone()
    if not student:
        print("Student not found.\n")
        return
    new_name = input("Enter New name:")
    new_age = input("Enter New age:")
    new_grade = input("Enter New grade:")

    try:
        cursor.execute('''
        UPDATE students
        SET name=?, age=?, grade=?
        WHERE id=?
        ''', (new_name, new_age, new_grade, student_id))
        conn.commit()

        print("\n✅ Student updated successfully.\n") 
    except sqlite3.IntegrityError: 
        print("\n❌ Name already exists.\n")

def delete_student():
    student_id = int(input("Enter student ID to delete: "))
    cursor.execute(
       "SELECT * FROM students WHERE id=?",
       (student_id,)
    )  

    student = cursor.fetchone()
    if not student:
        print("Student not found.\n")
        return
    cursor.execute(
       "DELETE FROM students WHERE id=?",
       (student_id,)
    )  
    conn.commit()

    print("\n✅ Student deleted successfully.\n")

while True:
    print("Student Management System")
    print("1. Add Student")
    print("2. View Students") 
    print("3. Update Student") 
    print("4. Delete Student") 
    print("5. Exit")

    choice = input("Enter Your Choice (1-5):")
    if choice == "1":
        add_student()

    elif choice == "2":
         view_student() 
    elif choice == "3":
         update_student()
    elif choice == "4": 
         delete_student() 
    elif choice == "5": 
        print("\n👋 Exiting Program...") 
        break 
    else: 
        print("\n❌ Invalid Choice. Try Again.\n")
conn.close()
print("Databse connection closed.")