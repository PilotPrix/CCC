liters = int(input("Amount of gas burned: "))
kilometers = int(input("Distance: "))

liters_per_100km = (liters / kilometers) * 100
print(str(liters_per_100km) + "L/100km")
