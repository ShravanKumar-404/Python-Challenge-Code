# Welcome to the python challenges of version 79.

"""Write a Python program that counts the number of vowels in a string recursively.

If the string is empty or only contains one consonant, print 0.

The program should be case-insensitive. Therefore, vowels in uppercase should also be counted."""

vowels = "Amazing".lower()


def vowel(x, y):
    v = ['a', 'e', 'i', 'o', 'u']
    if len(x) <= 1 and x not in v:
        return 0
    elif len(x) == 1 and x in v:
        return 1
    else:
        return y + vowel(x[y:-1], y+1)


def vowels2(x):
    v = ['a', 'e', 'i', 'o', 'u']
    if not x:
        return 0
    elif x[0] in v:
        return 1 + vowels2(x[1:])
    else:
        return vowels2(x[1:])
    pass


print(vowel(vowels, 0))
print(vowels2(vowels))
