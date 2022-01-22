prevDirection = ""
instruction = [""]

while True:
    num = input()
    direction = ""
    if num == "99999":
        break

    num1 = int(num[0])
    num2 = int(num[1])

    if num1 + num2 == 0:
        direction = prevDirection
    elif (num1 + num2) % 2 == 1:
        direction = "left"
    elif (num1 + num2) % 2 == 0:
        direction = "right"
    

    prevDirection = direction

    instruction.append(direction + " " + num[2:5])

for i in instruction:
    print(i)
