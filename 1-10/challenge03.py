"""
Write a Python Program that prints the reversed version of a string.

The program must preserve uppercase and lowercase letters.

If the string is empty, print it intact.

"""

word = "Hellooo"

if (len(word)==0):
  print("word is empty")
else:
  print(word[::-1])
  print("".join(reversed(word)))