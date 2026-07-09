"""
return vs print in Python

print() only displays output.
return sends a value back from a function so it can be reused.
"""

def print_square(number):
    print(number * number)


def return_square(number):
    return number * number


print_square(5)

result = return_square(5)
print("Returned result:", result)
print("Returned result used again:", result + 10)

# Bad approach if you need reuse:
# using only print means the value cannot be stored easily.
