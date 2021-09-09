"""

Write a Python program that prints the smallest value in a dictionary.

If the dictionary is empty, print None.

You may assume that the values are numeric.

"""
dicts2 = {"a": 4, "b": 8, "c": -1}
dicts3 = {}

if dicts2:
    print(min(set(dicts2.values())))
else:
    print(None)
