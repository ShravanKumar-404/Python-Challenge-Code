# Welcome to the python challenges of version 72.


"""
Write a Python program that finds the sum of a
list (or tuple) of numbers recursively.

Print the total sum.

If the list (or tuple) is empty, print 0.
"""

lists = list(range(1, 11))


def sums(s):
    if len(s) == 0:
        return 0
    else:
        return s[0] + sums(s[1:])


print(sums(lists))
