"""

Write a Python program that reverses the individual words in the string s and changes their capitalization. Uppercase letters should be printed in lowercase and vice versa.

Assume that the string only contains letters and spaces are used to separate words.

"""


word = "Python is Awesome"
new_word = ""

for i in word:
    if i == i.upper():
      new_word += i.lower()
    else:
      new_word += i.upper()
  
split_word = new_word.split(" ")
reverse_word = ""

for x in split_word:
  reverse_word += f"{x[::-1]} "
  
print(reverse_word)