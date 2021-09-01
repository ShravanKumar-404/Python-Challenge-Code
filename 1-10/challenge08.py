"""
- Write a Python program that prints the string s with the character curr_char replaced by the character new_char.

- curr_char and new_char are variables that contain strings with a single character.

- You may assume that new_char will not be an empty string.

- The match must be case-sensitive (do not replace lowercase letters if curr_char is uppercase).

- If no match is found, print the initial string.

"""

word = "Shravan"
curr_char = "a"
new_char = "v"

change_word = ""

for i in word:
  if i == curr_char:
    change_word += new_char
  else:
    change_word += i
    
print(change_word)
print(word.replace(curr_char, new_char))

