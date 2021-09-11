# Welcome to the python challenges of version 53.

"""

Write a Python program that prints the positive and negative solutions (roots)
for a quadratic equation.

If the equation only has one solution, print the solution as the output.

If it has two solutions, print the negative one first and the positive one second on the same line.

If the equation has no real solutions, print "Complex Roots".

You can determine the number of solutions with the discriminant
(the result of b^2 - 4ac in the formula below).

- If it's negative, the equation has no real solutions (only complex roots).

- If it's 0, there is only one solution.

- If it's positive, there are two real solutions.

"""
#       quadratic equation formula
#   x =  -b +- root of b square - 4ac
#                    2a

import math

a, b, c = 2, 5, -3

discriminant = b**2 - 4*a*c

if discriminant < 0:
    print("Complex Roots")
elif discriminant == 0:
    x = -b / (2*a)
    print(x)
else:
    x1 = (-b - math.sqrt(discriminant)) / (2*a)
    x2 = (-b + math.sqrt(discriminant)) / (2*a)
    print(x1, x2)
