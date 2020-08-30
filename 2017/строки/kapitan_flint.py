
# -*- coding:utf-8 -*-

x = 0
y = 0

while True:
	#прочитали одну строку в line
	line = raw_input()
	
	if line == 'Treasure':
		print x,y
		break
		
	# line разбили на части и каждую часть сделали int
	pair = line.split()
	direction = str(pair[0])
	print "my direction is ", direction
	d = int(pair[1])
	print "my distance is ", d
	
	if direction == 'north': # север
		y = y + d
	if direction == 'east':
		x = x + d
	if direction == 'west':
		x = x - d
	if direction == 'south':
		y = y -d

