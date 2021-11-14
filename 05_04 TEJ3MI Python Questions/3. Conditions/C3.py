while True:
    n = float(input("type in a number: "))
    userInput = input("would you like to convert into celcius or fahrenheit (c/f): ")
    if userInput == "f":
        print(str(n) + "C", "=", str((n * (9/5)) + 32) + "F")
        break
    elif userInput == "c":
        print(str(n) + "F", "=", str((n - 32) * 5/9) + "C")
        break
    else:
        print("try again")
        
