factors = []
sum = 0

input = input("Input a number: ")
input = int(input)

for i in range(1, input):
    if(input % i == 0):
        factors.append(i)

for i in range(len(factors)):
    sum += factors[i]

if(sum < input):
    print(input, "this is a deficient number")
elif(sum > input):
    print(input, "this is a abundant number")
else:
    print(input, "this is a composite number")