"""

Write a Python program that creates and print a dictionary 
that maps each element in a list to its corresponding frequency 
(how many times it occurs in the list).

The test should be case-sensitive.
Therefore, "A" should not be considered the same element as "a".

"""

# my method

# listA = ["a", "a", "b", "c", "a", "b", "d", "e", "d", "f"]
# listAA = [1, 2, 3, 4, 5, 1, 2, 7, 4, 5]

# listN = 0
# result = dict.fromkeys(listAA, listN)
# listB = list(result)

# for i in listAA:
#     if i in listB:
#         result[i] += 1

# print(result)

# method 2

listA = ["a", "a", "b", "c", "a", "b", "d", "e", "d", "f"]
result = {}

for i in listA:
    if i not in result:
        result[i] = 1
    else:
        result[i] += 1

print(result)
