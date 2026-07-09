"""
Lambda Functions in Python

A lambda function is a small anonymous function.
It is useful for short, simple operations.
"""

square = lambda number: number * number
add = lambda a, b: a + b
is_even = lambda number: number % 2 == 0

print("Square:", square(5))
print("Addition:", add(10, 20))
print("Is even:", is_even(8))

# Normal function version for comparison
def cube(number):
    return number ** 3

print("Cube:", cube(3))
