"""
Loops in Python

Loops are used to repeat code.
Python has two main loops:
- for loop
- while loop
"""

# for loop
for number in range(1, 6):
    print("For loop number:", number)

# while loop
count = 1
while count <= 5:
    print("While loop count:", count)
    count += 1

# break example
for number in range(1, 10):
    if number == 5:
        break
    print("Before break:", number)

# continue example
for number in range(1, 6):
    if number == 3:
        continue
    print("Skipping 3:", number)
