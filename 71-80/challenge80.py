# Welcome to the python challenges of version 80.


"""Write a Python program that prints the pattern of asterisks shown below for a given value of n.

The program must include a recursive function.

n represents the number of rows in the resulting pattern and the number of asterisks printed on the first row."""


n = int(input("Enter number of rows : "))


def asterisks(n):
    if n == 1:
        print("*")
    else:
        print("*"*n)
        asterisks(n-1)


asterisks(n)
