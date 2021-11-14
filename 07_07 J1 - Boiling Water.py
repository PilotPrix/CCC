B = input("Input the builing point in Celcius to calculate the atmospheric pressure: ")
B = int(B)
P = 5 * B - 400

print(P)
if(P > 100):
    print(-1)
elif(P == 0):
    print(0)
else:
    print(1)