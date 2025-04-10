""" WAP to implement following
(i) create dictionary
(ii)access elements from a dictionary
(iii) change or add elements in a dictionary
(iv) delete or remove elements from a dictionary
(v) find lenght and perform sorting
"""

# Branch:
# Year:
# Sem:
# Subject :
# Name:
# UIN:
# Roll No.:

print("***************************")
print("Dictionary Operations")
print("***************************")


while True:
    print("\n********** Dictionary Operations Menu **********")
    print("1. Create Dictionary")
    print("2. Access Elements from Dictionary")
    print("3. Change or Add Elements in Dictionary")
    print("4. Delete or Remove Elements from Dictionary")
    print("5. Find Length and Perform Sorting")
    print("6. Exit")
    print("***********************************************")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        my_dict = {}
        print("Empty Dictionary:", my_dict)
        my_dict = {1: 'apple', 2: 'ball'}
        print("Dictionary with Integer Keys:", my_dict)
        my_dict = {'name': 'John', 1: [2, 4, 3]}
        print("Dictionary with Mixed Keys:", my_dict)
        my_dict = dict({1:'apple', 2:'ball'})
        print("Using dict():", my_dict)
        my_dict = dict([(1,'apple'), (2,'ball')])
        print("From Sequence as Pairs:", my_dict)
    
    elif choice == '2':
        my_dict = {'name':'Jack', 'age': 26}
        print("Dictionary:", my_dict)
        print("Access name:", my_dict['name'])
        print("Access age:", my_dict.get('age'))
    
    elif choice == '3':
        my_dict = {'name':'Jack', 'age': 26}
        my_dict['age'] = 27
        print("Updated Age:", my_dict)
        my_dict['address'] = 'Downtown'
        print("After Adding Address:", my_dict)
    
    elif choice == '4':
        squares = {1:1, 2:4, 3:9, 4:16, 5:25}
        print("Dictionary Before Removal:", squares)
        print("Popped Element (Key 4):", squares.pop(4))
        print("Dictionary After pop(4):", squares)
        print("Popped Arbitrary Item:", squares.popitem())
        print("Dictionary After popitem():", squares)
        del squares[3]
        print("Dictionary After Deleting Key 3:", squares)
        squares.clear()
        print("Dictionary After clear():", squares)
    
    elif choice == '5':
        squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
        print("Length of Dictionary:", len(squares))
        print("Sorted Keys:", sorted(squares))
    
    elif choice == '6':
        print("Exiting Program. Goodbye!")
        break
    
    else:
        print("Invalid choice! Please enter a number between 1 and 6.")
print("Name: Shaikh Tasneem Azharul\nUIN: 231P043\nRoll No: 41")