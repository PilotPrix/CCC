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
    grid[i] = msg[i * rows_num, (i + 1) * rows_num]