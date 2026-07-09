"""
Recursion in Python

Recursion means a function calling itself.
Every recursive function must have a base condition.
"""

def factorial(number):
    if number == 0 or number == 1:
        return 1
    return number * factorial(number - 1)


def countdown(number):
    if number == 0:
        print("Done")
        return
    print(number)
    countdown(number - 1)


print("Factorial:", factorial(5))
countdown(5)
