# Voting eligibility
name = input("What's your name?\n")
age = int(input("How old are you?\n"))

if age >= 18:
    print("You may vote,", name)
else:
    n = 18 - age
    print("You may not vote", name + ".", "wait for", n, "years")
