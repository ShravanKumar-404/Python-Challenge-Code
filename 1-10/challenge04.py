"""
Write a Python program that prints the first and last three characters of the string s as a single string.

If the string has less than six characters, print an empty string (blank output).

"""

word = "ShravanKumar"

if len(word) < 6:
  print (" ")
else:
  print(word[0] + word[len(word)-3:])