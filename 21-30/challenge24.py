"""
Write a Python program that counts the number of elements in a list with value greater than 3.

You may assume that the list only contains numbers.

Print the final count.

"""
# my method
lists = [1, -1, 0, 2, 2, 3, 8, 100, 89]
number = 3
result = 0

for i in lists:
    if i > number:
        result += 1

print(result)

# method 2

lists = [1, -1, 0, 2, 2, 3, 8, 100, 89]
count = sum(1 for i in lists if i > number)
print(count)
