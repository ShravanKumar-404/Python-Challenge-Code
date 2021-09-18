# Welcome to the python challenges of version 75.

"""
Write a Python program that calculates and prints the sum of the digits of a positive integer num.

The program must find the sum recursively.

If the integer has only one digit, print the integer as the total sum.

"""

num = int(input("Enter the number : "))


def sums(num):
    if num == 0:
        return 0
    else:
        return (num % 10) + sums(num // 10)


print(sums(num))
