# Welcome to the python challenges of version 76.

"""
Write a Python program that find the value of a raised
to the power b recursively.

The operation is a**b in Python, where a is the base and b is the exponent.

If the value of b is 0, the result is automatically 1 because
every number raised to the power 0 is 1.
"""
a = int(input("Enter the base number : "))
b = int(input("Enter the power number : "))


def power(x, y):
    if y == 0:
        return 1
    else:
        return x * power(x, y-1)


print(power(a, b))
