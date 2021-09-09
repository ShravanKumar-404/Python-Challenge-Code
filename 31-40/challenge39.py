
"""
Write a Python program that counts the frequency of each value in a dictionary.
The program should create a new dictionary to map each value in the original dictionary to its frequency (how many times it occurs).
If the dictionary is empty, print an empty dictionary.
"""

my_dict = {"a": 4, "b": 4, "c": 2, "d": 7, "e": 4, "f": 2, "g": 7, "h": 7}

new_dict = {}

if my_dict:
    for i in my_dict.values():
        if i in new_dict:
            new_dict[i] += 1
        else:
            new_dict[i] = 1
    print(new_dict)
else:
    print("Empty")
