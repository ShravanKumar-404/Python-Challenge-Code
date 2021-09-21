# Welcome to the python challenges of version 71.
"""
Write a Python program that prints a diamond made with asterisks where the diamond's height (number of rows)
is determined by the value of the variable height

You can (optionally) ask the user to enter the value of height.

This value can only have an odd number of rows, so you should print a descriptive message if the user enters an even value.

"""


def odd_number_input():
    rows = int(input("Enter the odd number of rows : "))
    return odd_check(rows)


def odd_check(num):
    if num % 2 == 0:
        print("Number must be odd")
        odd_number_input()
    else:
        odd_number_above(num)


def odd_number_above(num):
    letter = "@"
    space = " "
    for x in range(1, num+1, 2):
        print(f"{space*(round((num-x)/2))}{letter*x}")

    odd_number_below(num, letter, space)


def odd_number_below(num, letter, space):
    number = 1
    for x in range(num-2, 0, -2):
        print(f"{space*number}{letter*x}")
        number += 1


odd_number_input()
