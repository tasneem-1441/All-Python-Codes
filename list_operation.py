''' WAP in python to implement following
    (i) create a list
    (ii) Display list
    (iii) Find length of list
    (iv)Check Element is in List or Not
    (v) Concatenating Lists in Python
    (vi) Replacing List Element with new one in Python
    (vii)Deleting Element from List in Python
    (viii) Python Nested Lists
'''
# Branch: Computer Engineering
# Year: 2nd year
# Sem: IV
# Subject : SKL Python
# Name: Shaikh Tasneem Azharul
# UIN: 231P043
# Roll No: 41

list1 = []
list2 = []

while True:
        
    print("****LIST OPERATIONS****")

    print("1.Create a list")
    print("2.Display list")
    print("3.Find length of list")
    print("4.Check Element is in List or Not")
    print("5.Concatenating Lists in Python")
    print("6.Replacing List Element with new one in Python")
    print("7.Deleting Element from List in Python")
    print("8.Create Nested Lists and display elements of nested list")
    print("9.Exit")

    choice = int(input("Enter your choice: "))
    
    if choice==9:
        print("Name: Shaikh Tasneem Azharul\nUIN: 231P043\nRoll No: 41")
        exit()
        break
            
    elif choice==1:
        print("Creating a list:")               
        element= input("Enter an element to add to the list:")
        print("In which list do you want to add your element, 1 or 2?")
        choice1 = int(input("Enter your list number:"))
        if choice1==1:
            list1.append(element)
        elif choice1==2:
            list2.append(element)
        else:
            print("Enter valid list number!")
        print(f"The element has been added!!")
        
    elif choice==2:
            choice2 = int(input("Enter the list you want to display: "))
            if choice2==1:
                 print(list1)
            else:
                 print(list2)
            print("List Displayed")

    elif choice==3:
            choice3 = int(input("Enter the list for which you want to check the lenght: "))
            if choice3==1:
                print(f"Lenght of the list1 is={len(list1)}")
            else:
                print(f"Lenght of the list2 is={len(list2)}")
            print("Done")

    elif choice==4:
            check_element=input("Enter an element you want to chcek: ")
            choice4 = int(input("Enter the list you want to chcek in: "))
            if choice4==1:
                if check_element in list1:
                    print(f"The {check_element} is in the list 1 !!!")
                else:
                    print(f"The {check_element} is not in the list 1 !!!")

            elif choice4==2:
                if check_element in list2:
                    print(f"The {check_element} is in the list 2 !!!")
                else:
                    print(f"The {check_element} is not in the list 2 !!!")
 
            else:
                print(f"The element is not in the list")

    elif choice==5:
        print(f"Conacatation of 2 lists are{list1+list2}")

    elif choice==6:
        index = int(input("Enter the index at which u want to replace:"))
        new_element= input("Enter the replace element: ")
        choice6=int(input("Enter the list you want to replace in: "))
        if choice6==1:
            if 0<=index<=len(list1):
                 list1[index]=new_element
                 print(list1) 
            else:
                 print("index not present!")
        elif choice6==2:
            if 0<=index<=len(list2):
                 list2[index]=new_element
                 print(list2)
            else:
                 print("index not present!")
        else:
             print("Index not present in both list!!")

    elif choice == 7:
        index = int(input("Enter the index that u want to delete:"))
        choice7=int(input("Enter the list you want to delete in: "))
        if choice7==1:
            if 0<=index<=len(list1):
                 list1.pop(index)
                 print(list1)
            else:
                 print("index not present!")
        elif choice7==2:
            if 0<=index<=len(list1):
                 list2.pop(index)
                 print(list2)
            else:
                 print("index not present!")
        else:
             print("Index not present in both list!!")
    
    elif choice==8:
         print("\nvii. Work with Nested Lists")
         books_list = [("C", 896), ("C++", 599), ("Python", 1269)]
         while True:
            print("\nNested List Operations:")
            print("1. Show Books List")
            print("2. Add a Book")
            print("3. Back to Main Menu")

            nested_choice = input("Enter your choice: ")

            if nested_choice == "1":
                print("\nBook\t\tPrice")
                for book, price in books_list:
                    print(f"{book}\t\t{price}")

            elif nested_choice == "2":
                book_name = input("\nEnter the name of the book: ")
                book_price = int(input("Enter its price: "))
                books_list.append((book_name, book_price))
                print("Book added successfully!")

            elif nested_choice == "3":
                break
    else:
        print("Invalid choice! Please try again.")
