#  https://dmoj.ca/problem/ccc21j4

order = []
count = 0
userInput = input()

for i in range(len(userInput)):
    order.append(userInput[i])

numOfS = 0
for i in range(len(order)):
    if order[i] == 'S':
        numOfS = numOfS + 1

for i in range(numOfS):
    # Check the for an S that has any other letters following it, the switch it with the last most one
    # repeat until there are no letters other than S following it
    
    if order[i] == "S":
        j = len(order) - 1
        while (j > i):
            if not order[j] == "S":
                count += 1
                temp = order[i]
                order[i] = order[j]
                order[j] = temp
                break

            j -= 1

print(order, count)

