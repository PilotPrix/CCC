meters = 100
seconds = 14

speed = (meters / 1000) / (seconds / 3600)
speed = round(speed * 100) / 100
print(str(speed) + "km/h")
