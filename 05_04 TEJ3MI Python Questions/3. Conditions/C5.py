import random
while True:
    x = random.randint(1, 100)
    y = random.randint(1, 100)

    if input("what's " + str(x) + " + " + str(y) + "?\n") == str(x + y):
        print("Correct!")
    else:
        print("Incorrect, it's " + str(x + y))
    
