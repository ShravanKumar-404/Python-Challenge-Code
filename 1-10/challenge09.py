"""
Write a Python program that prints a version of the string s with all commas replaced by dots.

"""

word = "Shravan, Kalyan, Krishna, Govindamma"

curr_char = ","
new_char = "."

replaced_word = ""

for i in word:
  if i == curr_char:
    replaced_word += new_char
  else:
    replaced_word += i
    
print(replaced_word)
print(word.replace(",","."))