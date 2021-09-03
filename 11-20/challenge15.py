"""

Write a Python program to count the number of repeated characters in the string s.

The program must print the total number of repeated characters and a message on the next line displaying the repeated characters separated by a space and sorted alphabetically.

If there are no repeated characters in the string, print 0 as the total count and None on the next line.

"""

word = "Shravan Kumar"

single = []
multiple = []


for x in word:
  if word.count(x) > 1 and x not in multiple:
    multiple.append(x)
  elif word.count(x) == 1:
    single.append(x)
  
print(f'Word - {word}')
print(f'Single letters - {"".join(single)}')
print(f'Multiple letters - {"".join(multiple)}')
print(f'Repeated letters - {len(multiple)}')
