# Welcome to the python challenges of version 60.

"""
Write a Python program that prints the multiplication table for a positive integer n.

The values displayed should go from n x 1 up to n x 10 with a descriptive format (as shown below).

Use a loop to implement your solution.

"""
print("==== Multiplication Table of 3 ====")
tables = int(input("Enter the table number : "))

for i in range(1, 11):
    print(f"{tables} x {i} = {tables*i}")
