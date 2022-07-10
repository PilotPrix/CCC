# https://dmoj.ca/problem/ccc16s3


# Data Collecction
userInput = input().split(" ")

N = int(userInput[0])
M = int(userInput[1])
Pho = []
paths = []

for i in input().split(" "):
    Pho.append(int(i))

# Receive the N - 1 paths
for i in range(N - 1):
    paths.append(input())

