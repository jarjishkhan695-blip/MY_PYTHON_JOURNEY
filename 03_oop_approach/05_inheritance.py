"""
Inheritance in Python

Inheritance allows one class to reuse the attributes and methods of another class.
"""

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("My name is", self.name)


class Student(Person):
    def study(self):
        print(self.name, "is studying Python")


student1 = Student("Jarjish")
student1.introduce()
student1.study()
