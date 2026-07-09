"""
OOP-Based Problem Solving

Here, problems are solved by grouping data and behavior into classes.
"""

class NumberTool:
    def __init__(self, number):
        self.number = number

    def multiplication_table(self):
        for i in range(1, 11):
            print(self.number, "x", i, "=", self.number * i)

    def count_digits(self):
        return len(str(abs(self.number)))

    def product_of_digits(self):
        product = 1
        for digit in str(abs(self.number)):
            product *= int(digit)
        return product


class TextTool:
    def __init__(self, text):
        self.text = text

    def is_palindrome(self):
        cleaned_text = self.text.lower().replace(" ", "")
        return cleaned_text == cleaned_text[::-1]


number_tool = NumberTool(1234)
number_tool.multiplication_table()
print("Digits:", number_tool.count_digits())
print("Product:", number_tool.product_of_digits())

text_tool = TextTool("madam")
print("Palindrome:", text_tool.is_palindrome())
