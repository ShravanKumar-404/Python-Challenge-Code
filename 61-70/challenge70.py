# Welcome to the python challenges of version 70.

"""
Write a Python program that prints a triangular pattern 
made with letters (as shown below).

The first row should have one letter A (in uppercase). 
The second row should have two letters B. 
The third row should have three letters C and so on.

The number of rows is determined by the value of n, 
which is entered by the user.

The letters must be separated by a space.
"""

rows = int(input("Enter the number of rows : "))
# letters = ""
# for x in range(65, 91):
#     letters += chr(x)

# number = 1
# for x in range(0, rows):
#     print(letters[x]*number)
#     number += 1

for i in range(0, rows):
    print(chr(65+i)*(i+1))
