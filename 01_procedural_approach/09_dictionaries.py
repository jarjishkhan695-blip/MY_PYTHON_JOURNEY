"""
Dictionaries in Python

A dictionary stores data in key-value pairs.
"""

student = {
    "name": "Jarjish",
    "age": 20,
    "course": "AI and Data Science"
}

print("Student:", student)
print("Name:", student["name"])
print("Age:", student.get("age"))

student["city"] = "Mumbai"
print("After adding city:", student)

student["age"] = 21
print("After updating age:", student)

for key, value in student.items():
    print(key, ":", value)
