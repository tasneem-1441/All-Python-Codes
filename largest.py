#Aim:Write a program in python to find largest between three number using functions.
# Branch: Computer Engineering
# Year: 2nd year
# Sem: IV
# Subject : SKL Python
# Name: Shaikh Tasneem Azharul
# UIN: 231P043
# Roll No: 41
def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
largest = find_largest(num1, num2, num3)
print(f"The largest number is: {largest}")
print("Name: Shaikh Tasneem Azharul\nUIN: 231P043\nRoll No: 41")
