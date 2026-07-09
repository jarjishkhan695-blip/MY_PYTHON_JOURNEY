"""
Basic Problem Solving using Procedural Approach

In procedural programming, we solve problems step by step.
"""

# 1. Print multiplication table
number = 5

print("Multiplication table of", number)
for i in range(1, 11):
    print(number, "x", i, "=", number * i)

# 2. Count digits in a number
num = 12345
count = 0
temp = num

while temp > 0:
    count += 1
    temp //= 10

print("Total digits:", count)

# 3. Product of digits
num = 1234
product = 1

temp = num
while temp > 0:
    digit = temp % 10
    product *= digit
    temp //= 10

print("Product of digits:", product)
