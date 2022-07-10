N = int(input())
fours = 0
fives = 0
possibilities = 0

sum = 0
a = int(N / 4)  # 4a is <= N
b = 0
# Check if 4a = N

Repeat = True
while Repeat:
    Repeat = False

    for i in range(a, -1, -1):
        b = a - i
        sum = 4 * i + 5 * b
        if sum == N:
            possibilities += 1

        if sum > N:
            Repeat = True
            a -= 1
            break

print(possibilities)