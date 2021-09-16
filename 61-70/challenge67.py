# Welcome to the python challenges of version 67.
"""
Write a Python program that prints a string reversed using a loop.

All the characters must be on the same line in reverse order.
"""

word = input("Enter the word : ")


letters = word[::-1]

for x in range(len(word)-1, -1, -1):
    print(word[x], end="")

print(letters)
