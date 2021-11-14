import math

while (True):
    r = int(input("type in a number: "))
    option = input("is this the radius or the diameter? (r/d)")
    if option == "d":
        r = r / 2
    
    a = math.pi * r ** 2
    c = 2 * math.pi * r

    print("radius: " + str(r) + "\narea: " + str(a) + "\ncircumference: " + str(c) + "\n")
