#Aim: Write a program to display first & last five elements of a data frame & show details of all attributes?
# Branch: Computer Engineering
# Year: 2nd year
# Sem: IV
# Subject : SKL Python
# Name: Shaikh Tasneem Azharul
# UIN: 231P043
# Roll No: 41
import pandas as pd
data = {
    'ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack'],
    'Age': [25, 30, 35, 40, 22, 28, 32, 26, 29, 27],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose'],
    'Salary': [50000, 60000, 70000, 80000, 55000, 65000, 75000, 85000, 72000, 78000]
}
df = pd.DataFrame(data)
print("First 5 Elements of DataFrame:")
print(df.head())
print("\nLast 5 Elements of DataFrame:")
print(df.tail())
print("\nDataFrame Information:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe())
print("Name: Shaikh Tasneem Azharul\nUIN: 231P043\nRoll No: 41")