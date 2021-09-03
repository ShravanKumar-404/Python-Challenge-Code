"""

Write a Python program to convert a string s to lowercase, sort the characters of each word in alphabetical order, and print the resulting string.

You may assume that the string only contains letters and spaces to separate the words.

Spaces should be preserved in the final string.

"""

word = "Hello World"
split_word = list(word.split(" "))

result = ""

for i in split_word:
  x = (list(i.lower()))
  print(x)
  
