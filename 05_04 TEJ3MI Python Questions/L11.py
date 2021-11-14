import time
import random

times = int(input("how many times should the die rolling be simulated?\n"))
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0

for i in range(times):
    r = random.randint(1, 6)
    if r == 1:
        a += 1
    if r == 2:
        b += 1
    if r == 3:
        c += 1
    if r == 4:
        d += 1
    if r == 5:
        e += 1
    if r == 6:
        f += 1


    
print("1 was rolled", a, "times (" + str(100 * a / times) + "%)")
print("2 was rolled", b, "times (" + str(100 * b / times) + "%)")
print("3 was rolled", c, "times (" + str(100 * c / times) + "%)")
print("4 was rolled", d, "times (" + str(100 * d / times) + "%)")
print("5 was rolled", e, "times (" + str(100 * e / times) + "%)")
print("6 was rolled", f, "times (" + str(100 * f / times) + "%)")
time.sleep(5)
