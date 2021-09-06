"""

Write a Python program that prints (as a list) the elements of listA that are not in listB as a list.

If the lists have the same elements, print an empty list.

If listA is an empty list, print an empty list.

"""

#  method 1


# list_a = [1, 2, 3, 4, 5]
# list_b = [1, 2]

# combined_list = []

# for x in list_a:
#     if x not in list_b:
#         combined_list.append(x)

# print(combined_list)

# method 2

# list_a = [1, 2, 3, 4, 5]
# list_b = [1, 2]

# combined_list = [x for x in list_a if x not in list_b]
# print(combined_list)

# method 3


list_a = [1, 2, 3, 4, 5]
list_b = [1, 2]

combined_list = list(set(list_a) - set(list_b))
print(combined_list)
