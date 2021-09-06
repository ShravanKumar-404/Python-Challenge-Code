"""
Write a Python program that prints a "flattened" version of a list that contains nested lists.

"Flattened" means that all the elements in the nested lists should be added to a main list 
such that it doesn't contain any nested lists, just the individual.

The list could contain other elements that are not lists or other sequences, 
so you must check the type of each element and act appropriately.

If the list is empty, print an empty list.

"""

listA = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
listB = [1, 2, 3, 4, 5, 6, [7, 8, 9]]
result = []

listC = str(listB)
listD = listC.replace("[", "")
listE = list(listD.replace("]", ""))
print(listC)
