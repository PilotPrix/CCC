def isConsonant(character):
    character = character.lower()
    isConsonant = True

    if character == "a":
        isConsonant = False
    elif character == "e":
        isConsonant = False
    elif character == "i":
        isConsonant = False
    elif character == "o":
        isConsonant = False
    elif character == "u":
        isConsonant = False
    elif character == "y":
        isConsonant = False

    return isConsonant

while True:
    x = input()
    if x == "quit!":
        break

    if len(x) > 4 and x[-2:] == "or" and isConsonant(x[-3:-2]):
        x = x[:-1] + 'u' + x[-1:]
        print(x)
    else:
        print(x)
    
    