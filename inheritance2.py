#""" Aim: WAP in python to implement following multiple inheritances"""
# Branch: Computer Engineering
# Year: 2nd year
# Sem: IV
# Subject : SKL Python
# Name: Shaikh Tasneem Azharul
# UIN: 231P043
# Roll No: 41

class Employee:
    def __init__(self,id):
        self.id=id
    def set_name(self,name):
            self.name=name
    def get_name(self):
            return self.name
    def get_id(self):
            return self.id

class Student:
    def __init__(self,coll_name):
        self.coll_name=coll_name
    def get_college_name(self):
          return self.coll_name
    def set_branch(self,branch):
          self.branch=branch
    def get_branch(self):
          return self.branch

class Intern(Employee,Student):
      def __init__(self, id,coll_name,period):
            Employee.__init__(self,id)
            Student.__init__(self,coll_name)
            self.period=period

      def setdetails(self,name,branch):
            super().set_name(name)
            super().set_branch(branch)

      def getdetails(self):
            print(f"ID        : {super().get_id()}")
            print(f"NAME        : {super().get_name()}")
            print(f"COLLEGE NAME        : {super().get_college_name()}")
            print(f"BRANCH        : {super().get_branch()}")
            print("PERIOD        :",self.period)

id = int(input("Enter your id: "))
college = input("Enter your college name: ")
period = int(input("Enter number of periods: "))    
name = input("Enter your name: ")
branch = input("Enter your branch: ")

i = Intern(id, college, period)
i.setdetails(name, branch)
i.getdetails()

print("Name: Shaikh Tasneem Azharul\nUIN: 231P043\nRoll No: 41")