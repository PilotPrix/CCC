x = int(input("starting number to convert to Fahrenheit:"))
y = int(input("ending number to convert to Fahrenheit: "))

for i in range(x, y + 1):
    print(str(i) + "C = " + str((i * 9/5) + 32) + "F")
    
