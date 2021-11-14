import math

while True:
    c1 = [int(input("x1: ")), int(input("y1: "))]
    c2 = [int(input("x2: ")), int(input("y2: "))]

    if abs(c1[0] - c2[0]) == abs(c1[1] - c2[1]):
        print("It's a square!")
    else:
        print("It's a rectangle!")
