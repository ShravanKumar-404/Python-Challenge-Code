# Welcome to the python challenges of version 73.

"""
Write a Python program that calculates and prints the nth Fibonacci number.

The value of n represents the position of the element in the sequence.

The initial value of n should be 0.

You may assume that the value of n is a non-negative integer.
"""
n = 10
lists = []

for x in range(0, n):
    if x == 0 or x == 1:
        lists.append(x)
    else:
        lists.append((lists[-1] + lists[-2]))

print(lists)
