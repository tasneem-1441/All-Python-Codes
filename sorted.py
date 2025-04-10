#Aim:WAP to create a user-defined exception where the program will ask the user to input a
#number again and again until the user enters the correct stored number.
# Branch: Computer Engineering
# Year: 2nd year
# Sem: IV
# Subject : SKL Python
# Name: Shaikh Tasneem Azharul
# UIN: 231P043
# Roll No: 41
class WrongNumberError(Exception):
    """Custom exception for incorrect number input"""
    pass

# Stored correct number
correct_number = 42  

while True:
    try:
        user_input = int(input("Enter the correct number: "))
        
        if user_input != correct_number:
            raise WrongNumberError("Incorrect number! Try again.")
        
        print("Congratulations! You entered the correct number.")
        break  # Exit loop when the correct number is entered

    except WrongNumberError as e:
        print(e)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
print("Name: Shaikh Tasneem Azharul\nUIN: 231P043\nRoll No: 41")