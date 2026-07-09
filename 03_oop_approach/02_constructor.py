"""
Constructor in Python

__init__() is a constructor.
It runs automatically when an object is created.
"""

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)


student1 = Student("Jarjish", 20)
student1.display_info()
