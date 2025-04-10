#Aim: Write a program to demonstrate Data Series and Data Frames using Pandas.
# Branch: Computer Engineering
# Year: 2nd year
# Sem: IV
# Subject : SKL Python
# Name: Shaikh Tasneem Azharul
# UIN: 231P043
# Roll No: 41
import pandas as pd
print(pd.__version__)
data_series = pd.Series([10, 20, 30, 40, 50], index=['A', 'B', 'C', 'D', 'E'])
print("Pandas Series:")
print(data_series)
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
data_frame = pd.DataFrame(data)
print("\nPandas DataFrame:")
print(data_frame)
print("\nAccessing the 'Name' column:")
print(data_frame['Name'])
print("\nAccessing row with index 2:")
print(data_frame.loc[2])
data_frame['Salary'] = [50000, 60000, 70000, 80000]
print("\nDataFrame after adding a new column:")
print(data_frame)
print("Name: Shaikh Tasneem Azharul\nUIN: 231P043\nRoll No: 41")