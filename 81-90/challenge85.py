# Welcome to the python challenges of version 85.
"""
Write a Python program that prints the last n lines 
of a text file in order.

The value of n should be provided by the user.

You may assume that n is a valid positive integer."""

num = int(input("Enter the number of lines : "))

with open("81-90/files/python.txt", "r") as file:
    content = file.readlines()
    if num <= len(content):
        for x in content[num:]:
            print(x, end="")
    else:
        print(f"Please enter line numbers below or equal to {len(content)}")
