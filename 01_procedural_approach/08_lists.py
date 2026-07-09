"""
Lists in Python

A list stores multiple values in a single variable.
Lists are mutable, meaning they can be changed.
"""

numbers = [10, 20, 30, 40, 50]

print("Original list:", numbers)
print("First item:", numbers[0])
print("Last item:", numbers[-1])

numbers.append(60)
print("After append:", numbers)

numbers.remove(20)
print("After remove:", numbers)

numbers.reverse()
print("After reverse:", numbers)

# Print only even numbers
for number in numbers:
    if number % 2 == 0:
        print("Even number:", number)
