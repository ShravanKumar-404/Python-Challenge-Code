"""

Write a Python program that checks if the string s starts with the sequence of characters denoted by the variable prefix.

If it does, print True. Else, print False.

This test should be case sensitive. For example, "A" should not be equivalent to "a".

If the length of the prefix is greater than the length of the string, print False.


"""

word = "Shravan"
prefixx = "Sh"

matched = ""

if len(word) > len(prefixx):
  for i in word[:len(prefixx)]:
    matched += i  
  print(matched == prefixx)
else:
  print(False)