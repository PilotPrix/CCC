import math

coordinate1 = [0, 0]
coordinate2 = [3, 4]

slope = (coordinate2[1] - coordinate1[1]) / (coordinate2[0] - coordinate1[0])
distance = math.sqrt((coordinate2[0] - coordinate1[0]) ** 2 +
                     (coordinate2[1] - coordinate1[1]) ** 2)

print("Slope:", slope)
print("Distance:", distance)
