# class person:

#     def __init__(self):
#         print("Hey i am a caretaker")
#     name = "hello"
#     occupation = "caretaker"
#     networth = 100
#     def info(self):
#         print(f"{self.name} is a {self.occupation} with a net worth of {self.networth}.")

# a = person()
# b = person()
# c = person()
# a.name = "Alice"
# a.occupation = "engineer"
# print(a.name , a.occupation)

# b.name = "Bob"
# b.occupation = "artist"
# c.name = "Charlie"
# c.occupation = "doctor"

# a.info()
# b.info()
# c.info()

# class person:

#     def __init__(self, n, o):
#         print("Hey i am a caretaker")
#         self.name = n
#         self.occupation = o
#         self.networth = 100
#     def info(self):
#         print(f"{self.name} is a {self.occupation} with a net worth of {self.networth}.")
# a = person("Alice", "engineer")
# b = person("Bob", "artist")
# a.info()
# b.info()

# class maths:
#     def __init__(self, num):
#         self.num = num

#     def addtonum(self, n):
#         self.num = self.num +n

#     @staticmethod
#     def add(a, b):
#         return(a + b)  
    
# a = maths(5)
# print(a.num)
# a.addtonum(6)
# print(a.num)

# class Employee:
#     company = "Amazon"
#     def show(self):
#         print(f"The name is {self.name} and the comapny is {self.company}")
#     def changecompany(cls, newcompany):
#         cls.company = newcompany
# e1 = Employee()
# e1.name = "harsh"
# e1.show()



class Student:
    def __init__(self, name , marks , branch):
        self.name = name 
        self.marks = marks 
        self.branch = branch

class Studentmanager:
    def __init__(self):
        self.students = []
    def add_student(self,name,marks ,branch):
        self.students.append({
            "name": name,
            "marks": int(marks),
            "branch": branch
        })

    def display_student(self):
        for student in self.students:
            print(f" name = {student['name']}, marks = {student['marks']} , branch = {student['branch']} ")

    def search_student(self, name):
        for student in self.students :
            if student['name'].lower() == name.lower():
                print(f" name = {student['name']}, marks = {student['marks']} , branch = {student['branch']} ")
                return
        print("Student not found")

    def delete_student(self,name):
        for student in self.students :
            if student['name'].lower() == name.lower():
                self.students.remove(student)
                print("student deleted")
                return
        print("Student not found")

    
    def save_student(self):
        with open("student.txt", 'w') as f:
            for student in self.students:
               f.write
               (f"{student['name']},{student['marks']},{student['branch']}\n")
        print("Students saved successfully.")

    def load_student(self):
        self.students.clear()

        try:
            with open("student.txt", "r") as f:
                for line in f:
                   name , marks , branch = line.strip().split(",")
           
                   self.students.append({
                          "name": name,
                          "marks": int(marks),
                          "branch": branch
                   })
            print("Students loaded successfully.")

        except FileNotFoundError:
            print("No saved file found.")

manager = Studentmanager()

s1 = Student("Shivam", 90, "CSE")
s2 = Student("rahul", 88, "SCEE")
s3 = Student("Priya", 91, "ECE")

manager.add_student(s1.name, s1.marks, s1.branch)
manager.add_student(s2.name, s2.marks, s2.branch)
manager.add_student(s3.name, s3.marks, s3.branch)


manager.display_student()

manager.search_student("Shivam")

manager.delete_student("Priya")
manager.display_student()
manager.save_student()
manager.load_student()
manager.display_student()





        
        

