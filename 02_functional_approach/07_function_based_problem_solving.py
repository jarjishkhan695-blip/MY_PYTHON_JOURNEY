"""
Function-Based Problem Solving

Here, problems are solved by breaking logic into reusable functions.
"""

def multiplication_table(number):
    for i in range(1, 11):
        print(number, "x", i, "=", number * i)


def count_digits(number):
    return len(str(abs(number)))


def product_of_digits(number):
    product = 1
    for digit in str(abs(number)):
        product *= int(digit)
    return product


def is_palindrome(text):
    cleaned_text = text.lower().replace(" ", "")
    return cleaned_text == cleaned_text[::-1]


multiplication_table(5)
print("Digits:", count_digits(12345))
print("Product:", product_of_digits(1234))
print("Palindrome:", is_palindrome("madam"))
