"""

Write a Python program that prints the elements of a list on the same line.

The elements should be separated only by a space (not by a comma).

The output should not include the opening and closing square brackets [ ].

"""

lists = [1, 2, 3, 4]
new_list = ""

# method 1
# for x in lists:
#   new_list += f"{x} "
# print(new_list)

# method 2

# for x in lists:
#   print(x, end = " ")
  
# method 3
print(*lists, sep= " ")