import math

m = int(input())
n = int(input())

validNum = 0

for i in range(m, n):
    digits = len(str(i))
    valid = True

    # checking each symmetrical digit pair one by one
    for I in range(math.ceil(digits / 2)):
        v = False
        
        # if beginning and end symmetrical digit are the same
        if str(i)[I] == str(i)[-1 - I]:
            # if they are equal to either 0, 1, or 8
            if str(i)[I] == '0' or str(i)[I] == '1' or str(i)[I] == '8':
                v = True

        if v == False:
            # if beginning and end symmetrical digit equals 6 and 9 respectively & vice versa
            if str(i)[I] == '6':
                if str(i)[-1 - I] == '9':
                    v = True
            if str(i)[I] == '9':
                if str(i)[-1 - I] == '6':
                    v = True
            # if not, the number is false
            if v == False:
                valid = False
                break
        
    if valid:
        # increment validNum each time the program finds a valid number
        validNum += 1

print(validNum)
