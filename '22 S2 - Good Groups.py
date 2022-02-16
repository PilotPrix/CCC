# Data collection
X = int(input())  # Same group
xPairs = []
for i in range(X):
    xPairs.append(input().split(" "))

Y = int(input())  # Different group
yPairs = []
for i in range(Y):
    yPairs.append(input().split(" "))

G = int(input())  # Groups
groups = []
for i in range(G):
    groups.append(input().split(" "))

violationCount = 0

# Check X restrictions
for i in xPairs:
    # find index of i[0] group[i]
    # find index of i[1] group[i]
    # if they don't match add to violationCount, then repead for each x pair

    pairInSameGroup = False

    for g in groups:  # g represents each individual group
        if i[0] in g and i[1] in g:
            pairInSameGroup = True
    
    if not pairInSameGroup:
        violationCount += 1

# Check Y restrictions
for i in yPairs:
    # find index of i[0] group[i]
    # find index of i[1] group[i]
    # if they match add to violationCount, then repead for each y pair

    pairInSameGroup = False

    for g in groups:  # g represents each individual group
        if i[0] in g and i[1] in g:
            pairInSameGroup = True
    
    if pairInSameGroup:
        violationCount += 1


print(violationCount)