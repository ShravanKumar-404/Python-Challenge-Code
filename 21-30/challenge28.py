"""

Write a Python program that prints the second largest value in a list.

If the list is empty or only has one element, print None.


"""

# my method

List = [1, 2, 3, 4, 5, 2, 3]


if len(List) > 1:
    listSet = set(List)
    setList = list(listSet)
    setList.sort(reverse=True)
    print(setList[1])
else:
    print(None)
