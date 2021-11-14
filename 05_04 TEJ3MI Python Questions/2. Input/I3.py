mealAmount = int(input("Meal amount: "))
tipPercentage = int(input("Tip percentage: ")) / 100

print("Meal Amount:", mealAmount)
print("tip amount:", tipPercentage * mealAmount)
print("Total:", mealAmount + (tipPercentage * mealAmount))
