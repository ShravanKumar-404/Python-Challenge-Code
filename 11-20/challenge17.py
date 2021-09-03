"""

Write a Python program that multiplies all the items in a list by the value of the variable factor.

The program must print the list as the output.

The program should also allow multiplying the variable factor by a string in case the list contains strings.

You may assume that the value of factor will be a positive integer.

"""

list_word = ["a", "b", "c"]
factors = 3


# method 1 
# new_list = []

# for i in list_word:
#   new_list.append(i*factors)
  
# method 2
for x in range(len(list_word)):
  list_word[x] *= factors
  
# method 3
# for x,y in enumerate(list_word):
#   list_word[x] = y * factors


print(list_word)
# print(new_list)