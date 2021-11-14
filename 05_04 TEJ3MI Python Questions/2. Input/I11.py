import math

coordinate1 = [int(input("x1: ")), int(input("y1: "))]
coordinate2 = [int(input("x2: ")), int(input("y2: "))]

slope = (coordinate2[1] - coordinate1[1]) / (coordinate2[0] - coordinate1[0])
distance = math.sqrt((coordinate2[0] - coordinate1[0]) ** 2 +
                     (coordinate2[1] - coordinate1[1]) ** 2)

print("Slope:", slope)
print("Distance:", distance)
