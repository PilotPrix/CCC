# https://dmoj.ca/problem/ccc14j3

rounds = int(input())  # total number of rounds
round = [[0, 0]] * rounds  # 2 numbers for each round
a = 0
b = 0

for i in range(rounds):
    round[i] = list(map(int, input().split(" ")))

for i in range(len(round)):
    if round[i][0] > round[i][1]:  # a wins
        b += round[i][0]
    elif round[i][0] < round[i][1]:  # b wins
        a += round[i][1]

print(100 - a)
print(100 - b)