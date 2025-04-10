#""" Aim:1. Write a program for single thread."""
# Branch: Computer Engineering
# Year: 2nd year
# Sem: IV
# Subject : SKL Python
# Name: Shaikh Tasneem Azharul
# UIN: 231P043
# Roll No: 41
print("Name: Shaikh Tasneem Azharul\nUIN: 231P043\nRoll No: 41")
import threading
import time
def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(1)
def print_letters():
    for letter in 'ABCDE':
        print(f"Letter: {letter}")
        time.sleep(1)
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Both threads have finished execution!")
