# Welcome to the python challenges of version 74.

"""
Write a Python program that calculates and prints the value of the factorial of the number num using recursion.

The factorial of a number x is denoted by x! and it is equal to x * (x-1) * (x-2) * ... * 1,
the product of all positive integers less than or equal to the number.

The value of 0! is equal to 1 by mathematical convention.
"""
num = int(input("Enter the number : "))


def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fac(n-1)


print(fac(num))
