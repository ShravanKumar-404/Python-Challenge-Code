"""

Write a Python program that creates and displays a dictionary that maps each letter
in a string to how many times the character occurs in the string (its frequency).

The dictionary should only include the characters in the string. 

The test should be case-insensitive ("A" should be counted as "a").

The keys in the dictionary should be lowercase letters.

Only include letters in the dictionary.

"""

my_name = "Shravan Kumar"
my_world = "Hello, World!"

name_dict = {}

for i in my_world.casefold():
    if i.isalpha():
        if i in name_dict:
            name_dict[i] += 1
        else:
            name_dict[i] = 1


print(name_dict)
