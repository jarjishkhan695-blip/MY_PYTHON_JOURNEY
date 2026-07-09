"""
map(), filter(), and reduce() in Python

These functions are used to process collections in a functional style.
"""

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# map: apply operation to every item
squares = list(map(lambda number: number * number, numbers))
print("Squares:", squares)

# filter: keep only matching items
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# reduce: combine all items into one value
total = reduce(lambda a, b: a + b, numbers)
print("Total:", total)
