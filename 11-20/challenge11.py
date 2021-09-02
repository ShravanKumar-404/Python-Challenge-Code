"""

Write a Python program that prints a copy of the string s without any spaces.

Words should be connected in the final string.

If the string doesn't contain spaces, print it intact

"""

word = " Shravan Kumar "
space = " "

new_word = ""

print(word.replace(space, ""))

for i in word:
  if i != space:
    new_word += i
  

print(new_word)