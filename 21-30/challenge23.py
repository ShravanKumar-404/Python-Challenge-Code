"""

Write a Python program that removes duplicate elements from a list, only keeping one occurrence of each element in the list.

The original list should be mutated (modified).

The program must print the final version of the list.

"""

lists = [1, 1, 2, 3, 4, 4]
no_duplicates_1 = list(set(lists))
no_duplicates_2 = list(dict.fromkeys(lists))
print(no_duplicates_1)
