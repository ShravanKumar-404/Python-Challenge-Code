"""

Write a Python program that creates and print a dictionary 
that maps each element in a list to its corresponding frequency 
(how many times it occurs in the list).

The test should be case-sensitive.
Therefore, "A" should not be considered the same element as "a".

"""

listA = ["a", "a", "b", "c", "a", "b"]
listN = 0
listB = set(listA)
result = dict.fromkeys(listB, listN)

for i in listA:
    if i in result.keys():
        result.update({i: listN + 1})

print(result)
