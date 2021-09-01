"""
Write a Python program that prints the first and last three characters of the string s as a single string.

If the string has less than six characters, print an empty string (blank output).

"""

word = "ShravanKumar"
charss = 7

if len(word) < charss*2:
  print (" oh no ")
else:
  print(word[:charss] + word[len(word)-charss:])
  
  
