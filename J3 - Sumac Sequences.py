# https://dmoj.ca/problem/ccc11j3

sequence = [0, 0]
sequence[0] = int(input())
sequence[1] = int(input())

i = 2
while True:
    sequence.append(sequence[i - 2] - sequence[i - 1])
    if sequence[i - 1] < sequence[i]:
        break
    i += 1


print(len(sequence))