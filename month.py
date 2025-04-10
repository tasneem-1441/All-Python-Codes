#Aim:Write a Program in python to demonstrate user defined exception. (month no.is input 1-12, above
#12 is exception).
# Branch: Computer Engineering
# Year: 2nd year
# Sem: IV
# Subject : SKL Python
# Name: Shaikh Tasneem Azharul
# UIN: 231P043
# Roll No: 41
class InvalidMonthError(Exception):
    """Custom exception for invalid month number"""
    pass
def get_month():
    try:
        month = int(input("Enter a month number (1-12): "))
        if month < 1 or month > 12:
            raise InvalidMonthError("Invalid month! Please enter a number between 1 and 12.")
        print(f"Month {month} is valid ✅")
    except InvalidMonthError as e:
        print(f"Error: {e}")
    except ValueError:
        print("Error: Please enter a valid integer.")
get_month()
print("Name: Shaikh Tasneem Azharul\nUIN: 231P043\nRoll No: 41")