"""

Write a Python program that prints the elements of a list followed their corresponding indices.

Each element and its index must be on the same line separated by a space.

If the list is empty, print "Empty List".

"""

# my method

lists = [1, 2, 3, 4]

for x, y in enumerate(lists):
  print(x, y)
  
# method 2 

for i in range(len(lists)):
  print(lists[i], i)