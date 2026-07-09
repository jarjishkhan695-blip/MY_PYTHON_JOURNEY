"""
Strings in Python

A string is a sequence of characters.
Strings are immutable, meaning they cannot be changed directly.
"""

text = "python programming"

print("Original:", text)
print("Uppercase:", text.upper())
print("Title case:", text.title())
print("Length:", len(text))
print("First character:", text[0])
print("Last character:", text[-1])
print("Slice:", text[0:6])
print("Replace:", text.replace("python", "Python"))

# Check palindrome
word = "madam"
if word == word[::-1]:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")
