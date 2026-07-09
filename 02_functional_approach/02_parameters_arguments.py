"""
Parameters and Arguments in Python

Parameters are variables written in a function definition.
Arguments are actual values passed to the function.
"""

def greet_user(name):
    print("Hello", name)


def add(a, b):
    return a + b


def student_info(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)


greet_user("Jarjish")
print("Sum:", add(10, 20))
student_info("Jarjish", 20, "AI and Data Science")
