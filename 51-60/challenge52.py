# Welcome to the python challenges of version 52.

"""
Write a Python program that determines if three numbers (a, b, and c) are in increasing order,
decreasing order, or none.

If a > b > c, print "Decreasing Order".

If a < b < c, print "Increasing Order".

Else, print "None". 

"""

x = (3, 2, 1)

if x[0] < x[1] < x[2]:
    print("increasing order")
elif x[0] > x[1] > x[2]:
    print("decreasing order")
else:
    print(None)
