#Aim:Write a program in Python that validates names and age as entered by the user to determine
#whether the person can cast vote or not using exception handling.
# Branch: Computer Engineering
# Year: 2nd year
# Sem: IV
# Subject : SKL Python
# Name: Shaikh Tasneem Azharul
# UIN: 231P043
# Roll No: 41
class InvalidNameError(Exception):
    """Custom exception for invalid name input"""
    pass
class InvalidAgeError(Exception):
    """Custom exception for invalid age input"""
    pass
def validate_voter():
    try:
        name = input("Enter your name: ").strip()
        age = input("Enter your age: ").strip()
        if not name.replace(" ", "").isalpha():
            raise InvalidNameError("Name must contain only alphabets and spaces.")
        if not age.isdigit():
            raise InvalidAgeError("Age must be a valid number.")
        age = int(age)
        if age < 18:
            raise InvalidAgeError("You must be at least 18 years old to vote.")
        print(f"Hello {name}, you are eligible to vote!")
    except InvalidNameError as e:
        print(f"Error: {e}")
    except InvalidAgeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
validate_voter()
print("Name: Shaikh Tasneem Azharul\nUIN: 231P043\nRoll No: 41")