import random

coinState = random.randint(1, 2)
x = input("Heads or Tails?: ").lower()

if x == "heads":
    if coinState == 1:
        print("Corrent! It was heads")
    else:
        coinState == 2;
        print("Incorrect, it was tales")
elif x == "tails":
    if coinState == 2:
        print("Corrent! It was heads")
    else:
        coinState == 1;
        print("Incorrect, it was tales")
else:
    print("please type in either heads or tales")
