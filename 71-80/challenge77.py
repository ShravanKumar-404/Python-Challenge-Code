# Welcome to the python challenges of version 77.

"""
Write a Python program that finds and prints the Greatest Common Divisor (GCD)
of the numbers a and b (the largest number that divides them both).
"""
import math

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(a, b))

print(math.gcd(a, b))
