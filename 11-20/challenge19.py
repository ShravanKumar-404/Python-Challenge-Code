"""

Write a Python program that prints the largest and smallest values in a list

Print the two values on the same line, separated by a space.

The largest value should appear first and the smallest value should appear second.

You may assume that the list only contains numeric values.

If the list is empty, print None.

"""

# my method

lists = [3, 7, 5, 6]

if lists == []:
  print(lists)
else:
  print(f"{max(lists)} {min(lists)}")
  


