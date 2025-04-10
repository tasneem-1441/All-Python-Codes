# Aim:Write a program to calculate volume of sphere using multilevel inheritance demonstrating method overriding.
# Branch: Computer Engineering
# Year: 2nd year
# Sem: IV
# Subject : SKL Python
# Name: Shaikh Tasneem Azharul
# UIN: 231P043
# Roll No: 41

class Radius:
    def __init__(self):
        self.radius = float(input("Enter the radius of the sphere: "))
    def calculate(self):
        print(f"Radius: {self.radius}")  # Base class method

class Area(Radius):
    def __init__(self):
        super().__init__()  # Calls the constructor of Radius to initialize self.radius
        self.area = 0
    def calculate(self):  # Method overriding
        self.area = 4 * 3.14 * self.radius ** 2
        print(f"Surface Area of the sphere: {self.area:.2f}")

class Volume(Area):
    def __init__(self):
        super().__init__()  # Calls the constructor of Area (which also calls Radius)
        self.volume = 0
    def calculate(self):  # Method overriding
        super().calculate()  # Calls the overridden method from Area class
        self.volume = (4 / 3) * 3.14 * self.radius ** 3
        print(f"Volume of the sphere: {self.volume:.2f}")

sphere = Volume()
sphere.calculate() 
print("Name: Shaikh Tasneem Azharul\nUIN: 231P043\nRoll No: 41")