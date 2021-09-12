# Welcome to the python challenges of version 59.

"""
Write a Python program that calculates and prints the
sum of the first 100 non-negative integers (from 1 to 100).

Use a loop to find this sum.

"""

# my method

output = 0

for i in range(1, 101):
    output += i

print(output)

# my method 2

print(sum(range(1, 101)))
