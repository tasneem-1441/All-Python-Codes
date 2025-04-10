#Aim:Write a program in Python to Perform following operations on file handling.
#1.Reading a file
#2.Writing to a file
#3.Appending to a file
# Branch: Computer Engineering
# Year: 2nd year
# Sem: IV
# Subject : SKL Python
# Name: Shaikh Tasneem Azharul
# UIN: 231P043
# Roll No: 41
def write_to_file(filename, content):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)
    print("✅ Data written successfully!")
def append_to_file(filename, content):
    """ Appends content to a file """
    with open(filename, "a", encoding="utf-8") as file:
        file.write(content)
    print("✅ Data appended successfully!")
def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            print("\n📖 File Content:\n")
            print(content)
    except FileNotFoundError:
        print("❌ Error: File not found!")
filename = "sample.txt"
write_to_file(filename, "Hello, this is a sample file.\nThis file is used for file handling operations.")
append_to_file(filename, "\nAppending a new line to the file.")
read_file(filename)
print("Name: Shaikh Tasneem Azharul\nUIN: 231P043\nRoll No: 41")