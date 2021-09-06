"""

Write a Python program that prints the second smallest value in a list.

If the list is empty or only has one element, print None.


"""


List = [0, 1, 2, 3, 4, 5, 2, 3]


if len(List) > 1:
    listSet = set(List)
    setList = list(listSet)
    print(setList[1])
else:
    print(None)
