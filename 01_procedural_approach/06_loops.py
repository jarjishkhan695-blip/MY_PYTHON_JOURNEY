"""
Loops in Python

Loops are used to repeat code.
Python has two main loops:
- for loop
- while loop
"""

# for loop
# for number in range(1, 6):
#     print("For loop number:", number)

# # while loop
# count = 1
# while count <= 5:
#     print("While loop count:", count)
#     count += 1

# # break example
# for number in range(1, 10):
#     if number == 5:
#         break
#     print("Before break:", number)

# # continue example
# for number in range(1, 6):
#     if number == 3:
#         continue
#     print("Skipping 3:", number)

# #Print all the nos from 1 to 10 

# for i in range(1,11):
#     print(i,end=" ")

# n=int(input("Enter your no:"))

# for i in range(1,11):
#     print(f"{n} x {i} = {n*i}")

## Print all even no between 1-100
 
# for i in range (1,101):
#     if i%2==0:
#         print(i)

## print odd
# for i in range(1,101):
#     if i%2!=0:
#         print(i)

## factorial
# n=int(input("Enter a no:"))
# fact=1
# for i in range(n,1,-1):
#     fact=i*fact
    
# print(fact)

##print factorial from 1-n
# n=int(input("Enter a no:"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
#     print(f"{i}! = {fact}")

## print all the prime nos 1-100
 
# for num in range (2,100):
#     prime=True

#     for i in range(2,num):
#         if num % i == 0:
#             prime=False

#     if prime:
#         print(num)

# for num in range(2,100):
#     prime=True

#     for i in range(2,num):
#         if num%i==0:
#             prime=False

#     if prime:
#         print(num)

# for num in range(2,101):
#     prime=True

#     for i in range(2,num):
#         if num%i==0:
#             prime=False
#     if prime:
#         print(num)

## check wether the given no is prime no

# n=int(input("Enter your no:"))

# if n<=1:
#     print("Enter the again")
# else:
#     prime=True

#     for i in range(2,n):
#         if n%i==0:
#             prime=False
#             break
#     if prime:
#         print("Prime")
#     else:
#         print("Not prime")

# n=int(input("Enter a no:"))

# if n<=1:
#     print("Prime")
# else:
#     prime=True
#     for i in range(2,n):
#         if n%i==0:
#             prime=False
#             break
#     if prime:
#         print("Prime")
#     else:
#         print("Not prime")

# for num in range(2,101):
#     prime=True

#     for i in range(2,num):
#         if num%i==0:
#             prime=False
#     if prime:
#         print(num)


n = int(input("Enter the no:"))

first=0
second=1
total=0

for i in range(n):
    print(first,end=" ")
    total=total+first

    next_no=first+second
    first=second
    second=next_no

print("Sum=",total)