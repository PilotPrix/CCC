position = 1

while True:
	x = int(input())
	if x == 0:
		print("You Quit!")
		break
	position = position + x
	if position == 9:
		position = 34
	elif position == 40:
		position = 64
	elif position == 67:
		position = 86
	elif position == 54:
		position = 19
	elif position == 90:
		position = 48
	elif position == 99:
		position = 77
	elif position > 100:
		position = position - x
	elif position == 100:
		print("You are now on square 100")
		print("You Win!")
		break
	print("You are now on square", position)