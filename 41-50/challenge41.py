"""

Write a Python program that prints the largest of the values in a dictionary.

You may assume that all the values in the dictionary are either lists or tuples.

"""
# my method


my_dict = {
    "a": [111, 211, 3],
    "b": [4, 0, -4],
    "c": [3, 5, 9],
    "d": [45, 12, 100]
}

if my_dict == {}:
    print("its empty")
else:
    new_list = max(sum(i) for i in my_dict.values())
    print(new_list)
