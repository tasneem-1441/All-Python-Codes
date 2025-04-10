''' WAP on set to perform following operations
    (i) create set
    (ii)union, intersection, difference, symmetric difference
    (iii) change set
    (iv) remove elements from a set
    (v) Use pop and clear
    (vi) test if an item exists in a set or not   
'''
# Branch: Computer Engineering
# Year: 2nd year
# Sem: IV
# Subject : SKL Python
# Name: Shaikh Tasneem Azharul
# UIN: 231P043
# Roll No: 41
print("************")
print("set Operations")
print("*************")
A, B = set(), set()
while True:
    print("\n********** Set Operations Menu **********")
    print("1. Create Sets")
    print("2. Union, Intersection, Difference, Symmetric Difference")
    print("3. Modify Set")
    print("4. Remove Elements from Set")
    print("5. Use Pop and Clear")
    print("6. Check if an Item Exists in a Set")
    print("7. Exit")
    print("*************************")
    choice = input("Enter your choice (1-7): ")
    if choice == '1':
        A = {0, 2, 4, 6, 8}
        B = {1, 2, 3, 4, 5}
        print("Set A:", A)
        print("Set B:", B)
    elif choice == '2':
        print("Union of A and B:", A | B)
        print("Intersection of A and B:", A & B)
        print("Difference of A and B (A - B):", A - B)
        print("Symmetric Difference of A and B:", A ^ B)
    elif choice == '3':
        my_set = {1, 3}
        print("Initial Set:", my_set)
        my_set.add(2)
        print("After Adding 2:", my_set)
        my_set.update([2, 3, 4])
        print("After Adding Multiple Elements:", my_set)
        my_set.update([4, 5], {1, 6, 8})
        print("After Adding List and Set:", my_set)
    elif choice == '4':
        my_set = {1, 3, 4, 5, 6}
        print("Initial Set:", my_set)
        my_set.discard(4)
        print("After Discarding 4:", my_set)
        my_set.remove(6)
        print("After Removing 6:", my_set)
        my_set.discard(2)  # No error if not present
        print("After Discarding 2:", my_set)
    elif choice == '5':
        my_set = set("HelloWorld")
        print("Initial Set:", my_set)
        print("Popped Element:", my_set.pop())
        print("Set after pop:", my_set)
        my_set.clear()
        print("Set after clear:", my_set)
    elif choice == '6':
        my_set = set("apple")
        print("Set:", my_set)
        print("Is 'a' in the set?", 'a' in my_set)
        print("Is 'p' not in the set?", 'p' not in my_set)
    elif choice == '7':
        print("Exiting Program. Goodbye!")
        print("Name: Shaikh Tasneem Azharul\nUIN: 231P043\nRoll No: 41")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 7.")