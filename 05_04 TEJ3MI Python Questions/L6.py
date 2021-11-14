import time

x = int(input("starting range: "))
y = int(input("ending range: "))

nSum = 0
for i in range(x, y + 1):
    print(i)
    nSum += i
print(nSum)
print("Done")
time.sleep(5)
