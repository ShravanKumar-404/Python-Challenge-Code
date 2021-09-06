# print all the prime numbers


num2 = int(input("Enter first number : "))
num3 = int(input("Enter last number number : "))

for i in range(num2, num3+1):
    if i >= 1:
        if (i == 1) or (i == 2):
            print(f"{i} is prime")
        elif(i % 2 == 0):
            print(f"{i} not prime")
        else:
            print(f"{i} is prime")
    else:
        print(f"{i} is not greater than 1")
