"""
Write a Python program that prints the corresponding season based on the value of the variable season_num.

The possible values of season_num are: 1 for Spring, 2 for Summer, 3 for Fall, 4 for Winter.

If the value of season_num is neither one of these values, print "Please enter a valid number".

"""

weeks = ["Monday", "Tuesday", "Wednesday",
         "Thursday", "Friday", "Saturday", "Sunday"]
weather = ["Spring", "Summer", "Fall", "Winter"]
number = 2

if number <= len(weather):
    print(f"{number}. {weather[number-1]}")
else:
    print("Please enter a valid number")
