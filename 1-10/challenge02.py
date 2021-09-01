"""
Write a Python program that prints the character at index i in the string s.

If the index is out of range, the program should print "i is out of range"

If the string is empty, the program should print "Empty String"

"""



word = "Helloooo"
index_number = 0

if (len(word) == 0):
  print("empty string")
elif (index_number < len(word)):
  print(word[index_number])
else:
  print("index is out of range")