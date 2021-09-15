# Welcome to the python challenges of version 65.

"""
Write a Python program that prints a triangular pattern 
like the ones shown below in the examples.

Each row must have its corresponding number of asterisks.
The first row contains one asterisk. The second row contains 
two asterisks. The third row contains three asterisks and so on.

The number of rows should be determined by the value of n,a value 
entered by the user.
"""
n = int(input("Enter the number of rows : "))
letter = "s"
space = " "
# i = 1
# while i <= n:
#     print(letter*i)
#     i += 1

for x in range(0, n)[1::2]:
    y = int((n-(x+1))/2)
    print(f"{space*y}{letter*x}{space*y}")
