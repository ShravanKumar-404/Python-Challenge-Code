# Welcome to the python challenges of version 64.

"""
Write a Python program that checks if a number is prime or not.

If the number is prime, it should print "Prime".

If the number is not prime, it should print "Not prime".

"""
"""
finding a the given number is prime number or not.

"""

num1 = int(input("Enter number : "))

# condition to check whether the number is greater than 1
# number must be divisible by itself and 1

if num1 >= 1:
    if (num1 == 1) or (num1 == 2) or num1 % 2 != 0:
        print("is prime")
    else:
        print("not prime")
else:
    print("number must be greater than 1")
