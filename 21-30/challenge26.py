"""

Write a Python program that calculates the distance between two 3D points.

The points are represented by two lists with three elements. The first element is the x-coordinate.
The second element is the y-coordinate. The third element is the z-coordinate

"""

# my method

pointA = [-3, 4, -5]
pointB = [2, 0, -4]

result = 0

# distance = ((pointA[0] - pointB[0])**2
#             + (pointA[1] - pointB[1])**2
#             + (pointA[2] - pointB[2])**2)**(1/2)

for i in range(3):
    result += ((pointB[i] - pointA[i])**2)

print(result**(1/2))
