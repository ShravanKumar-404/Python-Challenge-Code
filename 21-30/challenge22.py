"""

Write a Python program that removes all occurrences of the element elem_to_remove from a list.

The output of the program should be the new list with the element removed.

If the element is not found in the list, print the message "Not Found".

If the list is empty, print "Empty List".


"""

import string

# my method

# lists_numbers = []
# for x in range(1, 21):
#   lists_numbers.append(x)
  
# lists_alphabets = []
# for x in string.ascii_lowercase:
#   lists_alphabets.append(x)
  
# number_to_remove = 2
# alphabet_to_remove = "c"

# new_lists_numbers = []
# new_lists_alphabets = []

# for i in lists_numbers:
#   if i != number_to_remove:
#     new_lists_numbers.append(i)
    
# for i in lists_alphabets:
#   if i != alphabet_to_remove:
#     new_lists_alphabets.append(i)

# print(new_lists_numbers)
# print(new_lists_alphabets)

# my method 2

# list_numbers = []
# number_to_remove = 2



# if list_numbers == []:
#   print("empty")
# elif list_numbers.count(number_to_remove) == 0:
#   print("Not found")
# else:
#   result = []
#   for i in list_numbers:
#     if i != number_to_remove:
#       result.append(i)
#   print(result)

# method 3 

list_numbers = [1, 2, 2, 3]
number_to_remove = 2



if list_numbers == []:
  print("empty")
elif list_numbers.count(number_to_remove) == 0:
  print("Not found")
else:
  for i in range(list_numbers.count(number_to_remove)):
    list_numbers.remove(number_to_remove)
  print(list_numbers)
    