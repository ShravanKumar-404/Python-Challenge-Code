"""
finding a the given number is prime number or not.

"""

num1 = int(input("Enter number : "))

# condition to check whether the number is greater than 1
# number must be divisible by itself and 1

if num1 >= 1:
  if (num1 == 1) or (num1 == 2):
    print("is prime")
  elif(num1 % 2 == 0):
    print("not prime")
  else:
      print("is prime")
else:
  print("number must be greater than 1")

