# Welcome to the python challenges of version 66.

"""
Write a Python program that prints the digits of a number in reverse order on the same line.

If the number only has one digit, print this digit.

"""

num = input("Enter the number : ")

number = [i for i in num[::-1]]
reverse = num[::-1]

# awesome method for reverse algorithm it works for numbers

num1 = int(num)
reverse_num = 0

while num1 > 0:
    remainder = num1 % 10
    reverse_num = (reverse_num*10) + remainder
    num1 = num1 // 10

print("".join(number))
print(reverse)
print(reverse_num)
