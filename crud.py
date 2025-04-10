#Aim:WAP to demonstrate CRUD (create, read, update, delete) operation on database using sqlite3.
# Branch: Computer Engineering
# Year: 2nd year
# Sem: IV
# Subject : SKL Python
# Name: Shaikh Tasneem Azharul
# UIN: 231P043
# Roll No: 41
import sqlite3
conn = sqlite3.connect("students.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER,
                    grade TEXT)''')
conn.commit()
def insert_student(name, age, grade):
    cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
    conn.commit()
    print("Student added successfully.")
def fetch_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    print("\nStudents List:")
    for row in records:
        print(row)
def update_student(student_id, new_name, new_age, new_grade):
    cursor.execute("UPDATE students SET name = ?, age = ?, grade = ? WHERE id = ?", (new_name, new_age, new_grade, student_id))
    conn.commit()
    print("Student updated successfully.")
def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    print("Student deleted successfully.")
insert_student("Tasneem", 20, "A")
insert_student("Nausheen", 29, "B")
fetch_students()
update_student(1, "Shaziya", 25, "A+")
fetch_students()
delete_student(2)
fetch_students()
conn.close()
