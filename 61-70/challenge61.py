# Welcome to the python challenges of version 61.

"""
Write a Python program that prints all the letters in the alphabet using a loop (one letter per line).

The program should print the letters in uppercase.

"""

for i in range(65, 91):
    letter = chr(i)
    print(letter, ord(letter))

for i in range(97, 123):
    letter = chr(i)
    print(letter, ord(letter))
