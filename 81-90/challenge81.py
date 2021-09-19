# Welcome to the python challenges of version 81.


"""Write a Python program that converts a decimal number to binary using recursion.

The function must return the binary representation as a string.

The program must print the value returned."""

n = int(input("Enter the number : "))


def binaries(n):
    if n == 0:
        return 0
    else:
        return str(binaries(n//2)) + str(n % 2)


print(binaries(n)[1:])
