#""" Aim:Write a program to perform transpose of a matrix?
# Branch: Computer Engineering
# Year: 2nd year
# Sem: IV
# Subject : SKL Python
# Name: Shaikh Tasneem Azharul
# UIN: 231P043
# Roll No: 41
X = [[12,7],
    [4 ,5],
    [3 ,8]]
result = [[0,0,0],
         [0,0,0]]
for i in range(len(X)):
   for j in range(len(X[0])):
       result[j][i] = X[i][j]
for r in result:
   print(r)
print("Name: Shaikh Tasneem Azharul\nUIN: 231P043\nRoll No: 41")

