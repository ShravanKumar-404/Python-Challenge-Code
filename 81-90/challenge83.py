# Welcome to the python challenges of version 83.

"""
Write a Python program that reads a text file and saves its content line by line
to a list called file_content.

The list should contain strings that represent each line of the text file.

The program should print the resulting list."""

x = ["\nJava\n", "Javascript\n", "C-Sharp\n"]
with open("81-90/files/python.txt", "r") as file:
    print(file.readlines())
