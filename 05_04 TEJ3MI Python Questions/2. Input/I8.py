dozen_apple_price = float(input("Price of a dozen of apples: "))
apple_price = dozen_apple_price / 12
apple_count = int(input("How many apples would you like to purchase: "))

total = apple_count * apple_price

print("Your grand total is:", round((total) * 100) / 100)
