# Welcome to the python challenges of version 51.

"""
Write a Python program that prints the number of days in a given month.

The value of the variable month is the name of the month with the first letter capitalized.

Do not consider leap years for the number of days in February.

You can add a customized message. For example: "<month> has: <num_days> days."

"""


def months(month):
    monthss = {
        "January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31,
        "August": 31, "September": 30, "October": 31, "November": 30, "December": 31,
    }
    return monthss[month]


month = "october"
print(f"{month.capitalize()} has : {months(month.capitalize())} days")
