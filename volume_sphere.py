# Aim: Write a program to calculate volume of a sphere using multilevel inheritance.
# Branch: Computer Engineering
# Year: 2nd year
# Sem: IV
# Subject : SKL Python
# Name: Shaikh Tasneem Azharul
# UIN: 231P043
# Roll No: 41
class Radius:
    def __init__(self, radius):
        self.radius = radius
    def get_radius(self):
        return self.radius

class Area(Radius):
    def __init__(self, radius):
        super().__init__(radius)
        self.area = 0
    def calculate_area(self):
        pi = 3.14
        self.area = 4 * pi * self.radius * self.radius
    def get_area(self):
        return self.area

class Volume(Area):
    def __init__(self, radius):
        super().__init__(radius)
        self.volume = 0
    def calculate_volume(self):
        pi = 3.14
        self.volume = (4 / 3) * pi * self.radius * self.radius * self.radius
    def get_volume(self):
        return self.volume

class Display(Volume):
    def __init__(self, radius):
        super().__init__(radius)
        self.calculate_area()  # Calculate area when object is created
        self.calculate_volume()  # Calculate volume when object is created
    def display(self):
        print(f"Radius of the sphere: {self.get_radius()}")
        print(f"Area of the sphere: {self.get_area()}")
        print(f"Volume of the sphere: {self.get_volume()}")

radius = int(input("Enter the radius of the sphere: "))
sphere = Display(radius)
sphere.display()
print("\nName: Shaikh Tasneem Azharul")
print("UIN: 231P043")
print("Roll No: 41")
