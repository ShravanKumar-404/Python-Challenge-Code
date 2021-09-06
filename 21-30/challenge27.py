"""

Write a Python program that prints a list with the elements that listA and listB have in common.

If they don't have any elements in common, print an empty list.

The program should not assume that the lists have the same length.

You may assume that each element will only appear once in each list.


"""
# my method

# listA = [1, 2, 3]
# listB = [4, 5, 6]

# common = []

# for x in listA:
#     for y in listB:
#         if x == y:
#             common.append(x)

# print(common)

# method 2


listA = [1, 2, 3]
listB = [4, 5, 6]

common = []

for i in listA:
    if i in listB:
        common.append(i)

print(common)
