'''Program: WAP to perform following operation on queue
(i) Add
(ii) Delete
(iii) Search
(iv) Exit witout comments'''
# Branch: Computer Engineering
# Year: 2nd year
# Sem: IV
# Subject : SKL Python
# Name: Shaikh Tasneem Azharul
# UIN: 231P043
# Roll No: 41
class Queue:
    def __init__(self):
        self.queue = []
    def add(self, item):
        self.queue.append(item)
        print(f"{item} added to queue.")
    def delete(self):
        if not self.is_empty():
            print(f"Deleted element: {self.queue.pop(0)}")
        else:
            print("Queue is empty! Cannot delete.")
    def search(self, item):
        if item in self.queue:
            print(f"{item} found at position {self.queue.index(item) + 1}.")
        else:
            print(f"{item} not found in queue.")
    def is_empty(self):
        return len(self.queue) == 0
    def display(self):
        print("Queue:", self.queue if self.queue else "Queue is empty!")
queue = Queue()
while True:
    print("\nQueue Operations:")
    print("1. Add an element")
    print("2. Delete an element")
    print("3. Search an element")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        element = input("Enter element to add: ")
        queue.add(element)
    elif choice == 2:
        queue.delete()
    elif choice == 3:
        element = input("Enter element to search: ")
        queue.search(element)
    elif choice == 4:
        print("Exiting program.")
        print("Name: Shaikh Tasneem Azharul\nUIN: 231P043\nRoll No: 41")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 4.")
    queue.display()
