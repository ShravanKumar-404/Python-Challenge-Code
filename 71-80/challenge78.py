# Welcome to the python challenges of version 78.

"""
Write a Python program that checks if a string 
is a palindrome or not (if it's read the same backwards and forwards).

The program should be case-insensitive. 
Therefore, "A" should be considered equivalent to "a".

Print True if the string is a palindrome. Else, print False.

If the string is empty, print True.
"""

strings = "Anna".lower()


def palindrome(x):
    if len(x) <= 1:
        return True
    elif x[0] != x[-1]:
        return False
    else:
        return palindrome(x[1:-1])


print(palindrome(strings))
