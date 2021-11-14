import time

n = 0
while input("Can I have ice cream?\n").lower() != "yes":
    time.sleep(1)
    n += 1

print("Thankkk Youu")
time.sleep(0.5)
print("I've asked you " + str(n) + " times")
time.sleep(3)
