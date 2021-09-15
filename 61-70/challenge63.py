# Welcome to the python challenges of version 63.

"""
Write a Python program that calculates the factorial of a given number n.

The value of n should be entered by the user.

The program must print the result and use a loop to calculate it.

"""

import math

fac_num = int(input("Enter the Factorial Number : "))
multi_num = 1

for i in range(1, fac_num+1):
    multi_num *= i

print(multi_num)
print(math.factorial(fac_num))
