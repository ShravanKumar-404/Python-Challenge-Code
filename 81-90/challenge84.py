# Welcome to the python challenges of version 84.

"""
Write a Python program that reads a text file
and prints the first n lines of the file.

The value of n should be entered by the user.

If the value of n is greater than the total number of lines
in the file, print

"Please enter a value for n. The file has <num_lines> lines".
"""
num = int(input("Enter the number of lines : "))

with open("81-90/files/python.txt", "r") as file:
    content = file.readlines()
    if num <= len(content):
        for x in content[0:num]:
            print(x, end="")
    else:
        print(f"Please enter line numbers below or equal to {len(content)}")
