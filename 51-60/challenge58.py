# Welcome to the python challenges of version 58.

"""
Write a Python program that prints the integers between a given number n and 1 
(in descending order, both inclusive).

The value of n should be entered by the user and you may assume 
that it is an integer greater than or equal to 1.

Use a loop to print each number on a separate line.

"""
# my method 1

# num = input("Enter the number (number must be greater than 0): ")
# lists1 = list(range(1, int(num) + 1))
# lists1.sort(reverse=True)

# for i in lists1:
#     print(i)

# method 2

# num = input("Enter the number (number must be greater than 0): ")

# for i in range(int(num), 0, -1):
#     print(i)

# method 3

num = input("Enter the number (number must be greater than 0): ")

for i in reversed(range(1, int(num)+1)):
    print(i)
