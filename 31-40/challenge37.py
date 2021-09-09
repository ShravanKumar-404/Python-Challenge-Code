"""

Write a Python program that prints the largest value in a dictionary.

If the dictionary is empty, print None.

You may assume that the values are numeric.


"""

# my method

# dicts2 = {"a": 4, "b": 8, "c": 200}
# dicts3 = {}

# if dicts2 == {}:
#     print(None)
# else:
#     new_dicts2 = list(dicts2.values())
#     new_dicts2.sort()
#     print(new_dicts2[-1])

# method 2

dicts2 = {"a": 4, "b": 8, "c": 200}
dicts3 = {}

if dicts3:
    print(max(set(dicts2.values())))
else:
    print(None)
