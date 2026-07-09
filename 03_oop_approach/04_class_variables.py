"""
Class Variables in Python

Class variables are shared by all objects of a class.
"""

class Student:
    school_name = "Python Learning School"

    def __init__(self, name):
        self.name = name

    def display_info(self):
        print("Student Name:", self.name)
        print("School Name:", Student.school_name)


student1 = Student("Jarjish")
student2 = Student("Ali")

student1.display_info()
student2.display_info()
