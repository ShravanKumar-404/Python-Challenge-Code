"""

Write a Python program that checks if all values in a dictionary are equal.

If they are, print True. Else, print False.

If the dictionary is empty, print "Empty".


"""

dicts = {"a": 4, "b": 4, "c": 4}
dicts2 = {"a": 4, "b": 8, "c": 4}
dicts3 = {}

if dicts == {}:
    print("Empty")
else:
    print(len(set(dicts2.values())) == 1)
