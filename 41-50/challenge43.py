"""
Write a Python program that sorts (in ascending order) the lists contained as values in a dictionary.

The dictionary contains key-value pairs that match strings to lists. You need to sort these lists.

The lists have to be mutated (changed).

"""

# my method

# my_dict = {
#     "a": [4, 3, 2],
#     "b": [5, 3, 7],
#     "c": [1, 9, 10],
#     "d": [3, 4, 1]
# }

# if my_dict:
#     for i in my_dict:
#         x = my_dict.get(i)
#         x.sort()
#         my_dict[i] = x
#     print(my_dict)
# else:
#     print("its empty")

# method 2

my_dict = {
    "a": [4, 3, 2],
    "b": [5, 3, 7],
    "c": [1, 9, 10],
    "d": [3, 4, 1]
}

if my_dict:
    for i in my_dict.values():
        i.sort()
    print(my_dict)
else:
    print("its empty")
