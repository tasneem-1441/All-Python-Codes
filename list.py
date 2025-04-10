#Write a program to create a linked list and perform operation on list.without comments
# Branch: Computer Engineering
# Year: 2nd year
# Sem: IV
# Subject : SKL Python
# Name: Shaikh Tasneem Azharul
# UIN: 231P043
# Roll No: 41
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def delete_node(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
linked_list = LinkedList()
while True:
    print("\nLinked List Operations:")
    print("1. Insert at beginning")
    print("2. Insert at end")
    print("3. Delete a node")
    print("4. Search an element")
    print("5. Display list")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = input("Enter element to insert at beginning: ")
        linked_list.insert_at_beginning(data)
    elif choice == 2:
        data = input("Enter element to insert at end: ")
        linked_list.insert_at_end(data)
    elif choice == 3:
        key = input("Enter element to delete: ")
        linked_list.delete_node(key)
    elif choice == 4:
        key = input("Enter element to search: ")
        print("Element found" if linked_list.search(key) else "Element not found")
    elif choice == 5:
        linked_list.display()
    elif choice == 6:
        print("Name: Shaikh Tasneem Azharul\nUIN: 231P043\nRoll No: 41")
        break
    else:
        print("Invalid choice! Enter a number between 1 and 6.")
