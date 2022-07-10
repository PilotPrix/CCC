# https://dmoj.ca/problem/ccc16s2

maxMin = input()
N = int(input())

a = []
b = []

# convert string arrays into int arrays
for i in input().split(" "):
    a.append(int(i))
for i in input().split(" "):
    b.append(int(i))

if maxMin == "1":  # Min
    # Match the biggest pair from each list
    # Then the second biggest pair and so on
    a.sort()
    b.sort()

    # Take the highest value from each pair and add them up
    x = 0
    for i in range(N):
        x += max(a[i], b[i])
    print(x)
else:  # Max
    # Match the biggest and smallest from the first and second list respectively
    # Match the second biggest and smallest from each list
    a.sort()
    b.sort(reverse=True)

    x = 0
    for i in range(N):
        x += max(a[i], b[i])
    print(x)