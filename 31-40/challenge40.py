"""
Write a Python program that creates a dictionary from the values contained in nested lists.

Each nested list has this format [value1, value2].

value1 should be the key in the dictionary and value2 should be its corresponding value.

If there are no nested lists, print an empty dictionary.

"""

nested_lists = [["a", 1], ["b", 2], ["c", 3], ["d", 4]]

new_dict = {}

for i in nested_lists:
    if type(i) == list:
        new_dict[i[0]] = i[1]

print(new_dict)
