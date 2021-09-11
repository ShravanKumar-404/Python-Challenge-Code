# Welcome to the python challenges of version 55.

# Create a Calculator


import operator


def operation():
    print("Great! Now enter the operation. \nThese are the available options:")
    print("1 - Addition \n2 - Subtraction \n3 - Multiplication \n4 - Division \n5 - Integer Division \n6 - Modulo")
    operation1 = input("Please enter the operation to perform: ")

    while not operation1.isdigit() or int(operation1) > 6:
        print("Please enter valid operation to perform: ")
        operation2 = input("Please enter the operation to perform: ")
        if operation2.isdigit() and int(operation2) <= 6:
            return int(operation2)

    return int(operation1)


def first_number_check():
    number = input("Enter the First Number : ")
    while not number.isdigit():
        print("Please enter valid number")
        number1 = input("Enter the First Number : ")
        if number1.isdigit():
            return int(number1)
    return int(number)


def second_number_check():
    number = input("Enter the Second Number : ")
    while not number.isdigit():
        print("Please enter valid number")
        number1 = input("Enter the Second Number : ")
        if number1.isdigit():
            return int(number1)
    return int(number)


def exit():
    rcalc = input(
        "To repeat calculation , type 'y' to continue or 'n' to exit : ")
    if rcalc == 'y' and rcalc.isalpha():
        calculator()
    elif rcalc.isnumeric():
        print("Sorry You entered number..\nThanks for the calculation.. \nBYE BYE")
    else:
        print("Thanks for the calculation............... \nBYE BYE")


def calculator():
    fnum = first_number_check()
    snum = second_number_check()
    opera = operation()

    if opera == 1:
        print(f"addition of {fnum}+{snum} : {fnum + snum}")
        print(".\n.\n.\n")
        exit()
    elif opera == 2:
        print(f"subtraction of {fnum}+{snum} : {fnum - snum}")
        exit()
    elif opera == 3:
        print(f"multiplication of {fnum}*{snum} : {fnum * snum}")
        exit()
    elif opera == 4:
        if snum == 0:
            print("Cannot divide by Zero")
            exit()
        else:
            print(f"division of {fnum}/{snum} : {fnum / snum}")
            exit()
    elif opera == 5:
        if snum == 0:
            print("Cannot divide by Zero")
            exit()
        else:
            print(f"integer division of {fnum}//{snum} : {fnum // snum}")
            exit()
    elif opera == 6:
        print(f"modulo of {fnum}%{snum} : {fnum % snum}")
        exit()


def repeat_calc():
    calculator()


calculator()
