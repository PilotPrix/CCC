# https://dmoj.ca/problem/ccc04j4
import math

key = input()
msg = input()
grid = []

def letterIndex(x) -> int:
    return "abcdefghijklmnopqrstuvwxyz".find(x)


# seperate into columns of length of key variable

rows_num = math.ceil(len(msg) / len(key))
for i in range(rows_num):
    grid.append(msg[i * len(key):(i + 1) * len(key)])
print(grid)