#  https://dmoj.ca/problem/ccc21j2

numOfBidders = int(input())
winner = ""
winnerBidAmount = 0

for i in range(numOfBidders):
    name = input()
    bidAmount = int(input())

    if winnerBidAmount < bidAmount:
        winnerBidAmount = bidAmount
        winner = name

print(winner)