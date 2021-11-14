x = int(input())
m = int(input())
n = 0

for i in range(m):
    if (x * i) % m == 1:
        n = i

if n:
    print(n)
else:
    print("No such integer exists.")