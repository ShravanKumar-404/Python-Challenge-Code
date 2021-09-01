"""

Write a Python program that prints the string s without the character at index n.

If the index n is out of range, print the string s intact.

If the string s is empty, print the string s intact.


"""

word = "Shravan"
num = 1

if len(word) < num:
  print(word)
else:
  print(word[:num] + word[num+1:])
  
  
if len(word) == 0 or len(word) < num:
  print(word)
else:
  words = ""
  for i in range(len(word)):
    if i == num:
      pass
    else:
      words += word[i]
  print(words)