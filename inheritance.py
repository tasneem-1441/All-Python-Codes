#""" Aim: WAP in python to implement following inheritances"""
# Branch: Computer Engineering
# Year: 2nd year
# Sem: IV
# Subject : SKL Python
# Name: Shaikh Tasneem Azharul
# UIN: 231P043
# Roll No: 41
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display(self):
        super().display()
        print(f"Student ID: {self.student_id}")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display(self):
        super().display()
        print(f"Subject: {self.subject}")

# Example Usage
s = Student("Shaikh Tasneem\n", 20, "S1234")
t = Teacher("Mohd Ashfaque", 40, "Mathematics")

print("\nStudent Details:")
s.display()

print("\nTeacher Details:")
t.display()
print("Name: Shaikh Tasneem Azharul\nUIN: 231P043\nRoll No: 41")