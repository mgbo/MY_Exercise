
# -*- coding:utf-8-*-

x=0
y=0

while True:
	line = input() # прочитали одну строку в line
	if line=='Treasure':
		print (x,y)
		break
	
	pair = line.split()
	direction = pair[0]
	d = int(pair[1])

	if direction=="north":
		y+=d
	elif direction=="south":
		y-=d
	elif direction=="eath":
		x+=d
	elif direction=="west":
		x-=d

