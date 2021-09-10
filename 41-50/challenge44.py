"""

Write a Python program that takes the content of a dictionary and converts it into a list of lists.

Each nested list should contain a key as the first element and its corresponding value
as the second element.

Print the final list of lists.

"""
# my method


# product_info = {
#     "description": "shoe",
#     "price": 4.56,
#     "colors": ["green", "blue", "red"],
# }
# new_list = []
# for i in product_info:
#     lists = []
#     lists.append(i)
#     lists.append(product_info[i])
#     new_list.append(lists)

# print(new_list)


# my method 2


# product_info = {
#     "description": "shoe",
#     "price": 4.56,
#     "colors": ["green", "blue", "red"],
# }

# result = []

# for i in product_info.items():
#     result.append(list(i))

# print(result)


# my method 3

product_info = {
    "description": "shoe",
    "price": 4.56,
    "colors": ["green", "blue", "red"],
}

result = [[key, value] for key, value in product_info.items()]
print(result)
