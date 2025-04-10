""" WAP to perform following operation on stack
1. push an element
2. pop an element
3. peep an element
4. search an element
5. Exit
"""
# Branch: Computer Engineering
# Year: 2nd year
# Sem: IV
# Subject : SKL Python
# Name: Shaikh Tasneem Azharul
# UIN: 231P043
# Roll No: 41
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        """Push an element onto the stack."""
        self.stack.append(item)
        print(f"{item} pushed to stack.")

    def pop(self):
        """Pop an element from the stack."""
        if not self.is_empty():
            print(f"Popped element: {self.stack.pop()}")
        else:
            print("Stack is empty! Cannot pop.")

    def peep(self):
        """Peep (view) the top element of the stack."""
        if not self.is_empty():
            print(f"Top element: {self.stack[-1]}")
        else:
            print("Stack is empty! No top element.")

    def search(self, item):
        """Search for an element in the stack."""
        if item in self.stack:
            position = len(self.stack) - self.stack.index(item)
            print(f"{item} found at position {position} from top.")
        else:
            print(f"{item} not found in stack.")

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def display(self):
        """Display the stack."""
        if not self.is_empty():
            print("Stack (top to bottom):", self.stack[::-1])
        else:
            print("Stack is empty!")
stack = Stack()
while True:
    print("\nStack Operations:")
    print("1. Push an element")
    print("2. Pop an element")
    print("3. Peep (view top element)")
    print("4. Search an element")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        element = input("Enter element to push: ")
        stack.push(element)
    elif choice == 2:
        stack.pop()
    elif choice == 3:
        stack.peep()
    elif choice == 4:
        element = input("Enter element to search: ")
        stack.search(element)
    elif choice == 5:
        print("Exiting program.")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
      
    stack.display()
