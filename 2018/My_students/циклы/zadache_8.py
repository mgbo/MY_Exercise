
x = 0
y = 0

while  True:
	line = input()
	if line == 'Treasure!':
		print (x,y)
		break

	direction,d = line.split()

	if direction=="east":
		x = x + int(d)

	elif direction=="west":
		x = x - int(d)

	elif direction=="north":
		y = y + int(d)

	elif direction=="south":
		y = y - int(d)

