#""" Aim: Write a Program to make simple calculator using if statements """
# Branch: Computer Engineering
# Year: 2nd year
# Sem: IV
# Subject : SKL Python
# Name: Shaikh Tasneem Azharul
# UIN: 231P043
# Roll No: 41
print("******Welcome to Calculator!!*****")

while True:

    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")

    choice = int(input(("Please enter your choice: ")))
 
    if choice==5:
        print("Name: Shaikh Tasneem Azharul\nUIN: 231P043\nRoll No: 41")
        break

    if choice>=1 and choice <=4:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        if choice==1:
            res = num1+num2
            print("Result= ",res)

        elif choice==2:
            res = num1-num2
            print("Result= ",res)

        elif choice==3:
            res = num1*num2
            print("Result= ",res)

        elif choice==4:
            res = num1/num2
            print("Result= ",res)

    else:
        print("Wrong Input!!Try Again!!")