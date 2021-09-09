"""
Write a Python program that merges 
two dictionaries and prints the resulting dictionary.

"Merging" the dictionaries involves making a new dictionary with the key-value pairs
in both dictionaries.

"""

# my method

# my_dict1 = {"a": 1, "b": 2, "c": 3}
# my_dict2 = {"c": 4, "d": 6, "e": 8}

# my_dict1.update(my_dict2)
# print(my_dict1)

# method 2

# my_dict1 = {"a": 1, "b": 2, "c": 3}
# my_dict2 = {"c": 4, "d": 6, "e": 8}

# new_dict = {**my_dict1, **my_dict2}

# print(new_dict)

# method 3

my_dict1 = {"a": 1, "b": 2, "c": 3}
my_dict2 = {"c": 4, "d": 6, "e": 8}

new_dict = my_dict1 | my_dict2

print(new_dict)
