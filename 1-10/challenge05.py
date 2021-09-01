"""
Write a Python program that prints the string s without the characters located at even indices.

If the string is empty or only has one character, print it intact.

"""



word = "Shravan"

if len(word) > 1:
  print(word[1::2])
else:
  print(word)
  
words = ""

for i in range(1,len(word),2):
  words += word[i]
  
print(words)

  
  