#""" Aim: Program: You're going to write an interactive calculator! """
# Branch: Computer Engineering
# Year: 2nd year
# Sem: IV
# Subject : SKL Python
# Name: Shaikh Tasneem Azharul
# UIN: 231P043
# Roll No: 41
class FormulaError(Exception):
    """Custom exception for invalid formulas"""
    pass

def calculate(expression):
    parts = expression.split()
    
    if len(parts) != 3:
        raise FormulaError("Input must contain exactly 3 elements: number operator number")
    
    num1, operator, num2 = parts

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        raise FormulaError("The first and third elements must be numbers")

    if operator not in ('+', '-'):
        raise FormulaError("Operator must be '+' or '-'")

    return num1 + num2 if operator == '+' else num1 - num2

# Interactive loop
while True:
    user_input = input(">>> ")
    if user_input.lower() == "quit":
        break
    try:
        result = calculate(user_input)
        print(result)
    except FormulaError as e:
        print(f"Error: {e}")

print("Name: Shaikh Tasneem Azharul\nUIN: 231P043\nRoll No: 41")