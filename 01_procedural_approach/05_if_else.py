"""
Conditional Statements in Python

if, elif, and else are used to make decisions.
"""

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")

# Example with logical operators
age = 20
has_id = True

if age >= 18 and has_id:
    print("Allowed")
else:
    print("Not allowed")
