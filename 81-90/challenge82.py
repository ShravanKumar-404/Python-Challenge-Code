# Welcome to the python challenges of version 82.

"""Write a Python program that implements the Binary Search algorithm recursively.

The function should search for an element in a list or sequence and return its index.

If the element is not found, the value returned should be -1."""


lists = list(range(1, 21))
n = int(input("Enter the number from the list = 1 to 20 :  "))


def find_binary(lists, low, high, num):
    if low > high:
        return -1
    else:
        mid = (low + high) // 2
        if lists[mid] == num:
            return mid
        elif num < lists[mid]:
            return find_binary(lists, low, mid - 1, num)
        else:
            return find_binary(lists, mid - 1, high, num)


print(find_binary(lists, low=0, high=len(lists), num=n))
