# Welcome to the python challenges of version 69.

"""
Write a Python program that prints Floyd's Triangle with n number of rows.

The value of n should be entered by the user. You may assume that it is a positive integer.

Floyd's Triangle is made with consecutive numbers that fill the rows of the triangle (as shown below).
"""
rows = int(input("Enter th number of rows : "))
letters = "*"
number = 1
lists = [i*letters for i in range(1, rows+1)]
list3 = []

# for x in lists:
#     if len(x) == 1:
#         print(1)
#     elif len(x) > 1:
#         list2 = []
#         for i in x:
#             list2.append(number)
#             number += 1
#         y = (str(list2))[1:-1]
#         z = y.replace(",", "")
#         print(z)

for i in range(1, rows+1):
    for x in range(0, i):
        print(number, end=" ")
        number += 1
    print()
