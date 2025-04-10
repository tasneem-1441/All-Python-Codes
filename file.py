#Aim:Python program to count number of lines, words and characters in a file.
# Branch: Computer Engineering
# Year: 2nd year
# Sem: IV
# Subject : SKL Python
# Name: Shaikh Tasneem Azharul
# UIN: 231P043
# Roll No: 41
def count_file_content(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
            num_chars = sum(len(line) for line in lines)

        print(f"Lines: {num_lines}")
        print(f"Words: {num_words}")
        print(f"Characters: {num_chars}")
    except FileNotFoundError:
        print("File not found. Please provide a valid filename.")

# Example usage
filename = "sisters1.txt"  # Replace with your file name
count_file_content(filename)
print("Name: Shaikh Tasneem Azharul\nUIN: 231P043\nRoll No: 41")
