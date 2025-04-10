''' WAP to perform following operations on tuple
    (i)Create tuple
    (ii) Dispplay tuple
    (iii) Find Length of Tuple in Python
    (iv) Check Element Present in Tuple or Not
    (v) Concatenating Tuples in Python
    (vi)Deleting a Tuple
    (vii)use count method
'''
# Branch: Computer Engineering
# Year: 2nd year
# Sem: IV
# Subject : SKL Python
# Name: Shaikh Tasneem Azharul
# UIN: 231P043
# Roll No: 41

tuple1 = ("Nazrana", "Tarana", "Farzana", "Talat")
tuple2 = ("Daraksha", "Shaziya", "Nausheen", "Tasneem")

while True:
        
    print("****TUPLE OPERATIONS****")

    print("1.Create a tuple")
    print("2.Display tuple")
    print("3.Find length of tuple")
    print("4.Check Element is in tuple or Not")
    print("5.Concatenating tuple in Python")
    print("6.Deleting a Tuple")
    print("7.Use count method to count a count the element in the tuple")
    print("8.Exit")

    choice = int(input("Enter your choice: "))

    if choice==1:
        choice1= int(input("Enter the which tuple you want to create:"))
        if choice1==1:
            tupple1 = ("Nazrana", "Tarana", "Farzana", "Talat")
            print("Tuple 1 Created")
        elif choice1==2:
            tupple2 = ("Daraksha", "Shaziya", "Nausheen", "Tasneem")
            print("Tuple 2 Created")
        else:
            print("Enter a valid tuple number!!")

    elif choice==2:
        choice2 =int(input("Enter the tuple number you want to display: "))
        if choice2==1:
            print(tuple1)
            print("Tuple 1 Displayed")

        elif choice2==2:
            print(tuple2)
            print("Tuple 2 Displayed")

        else:
            print("Enter a valid tuple number!!")

    elif choice ==3:
        choice3 =int(input("Enter the tuple for which you want to check the lenght of: "))
        if choice3==1:
            print(f"The lenght of tuple 1 is {len(tuple1)}")
        elif choice3==2:
            print(f"The lenght of tuple 2 is {len(tuple2)}")
        else:
            print("Enter a valid tuple number!!")

    elif choice==4:
        check_element= input("Enter the element you want to check: ")
        choice4= int(input("Enter the tuple in which you want to chcek the element: "))
        if choice4==1:
            if check_element in tuple1:
                print(f"The element {check_element} is in the tuple 1")
            else:
                print(f"The element {check_element} is not in the tuple 1")
        elif choice4==2:
            if check_element in tuple2:
                print(f"The element {check_element} is in the tuple 2")
            else:
                print(f"The element {check_element} is not in the tuple 2")
        else:
            print("Enter a valid tuple number!!")

    elif choice==5:
        print(f"Concatation of tuples is {tuple1+tuple2}")

    elif choice==6:
        choice6=int(input("Enter the tuple which you want to delete: "))
        if choice6==1:
            del tuple1
            print("Tuple 1 deleted")
        elif choice6==2:
            del tuple2
            print("Tuple 2 deleted")
        else:
            print("Enter a valid tupple number!!")

    elif choice==7:
        element = input("\nEnter the element to count: ")
        count = tuple2.count(element)
        print(f"\n'{element}' appears {count} times in the tuple.")
    elif choice==8:
        print("Name: Shaikh Tasneem Azharul\nUIN: 231P043\nRoll No: 41")
        exit()

    else:
        print("Enter a valid input!!")
        