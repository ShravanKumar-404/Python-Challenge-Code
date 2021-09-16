# Welcome to the python challenges of version 68.

"""
Write a Python program that prints a pyramid pattern made with asterisks.

The number of rows should be determined by the value of the variable n. This value will be entered by the user.

You may assume that the value of n is a positive integer.

"""

n = int(input("Enter the number of rows : "))
letter = "s"
space = " "

for x in range(1, n):
    print(f"{space*(n-x)}{x*letter}")
