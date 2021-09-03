"""

Write a Python program that checks if a list is empty or not.

If the list is empty, print "Empty". Else, print "Not Empty".


"""

# my method

lists = []

if lists == [] or len(lists) == 0:
  print("empty")
else:
  print("not empty")
  
  
# method 2

if lists:
  print("not empty")
else:
   print("empty")