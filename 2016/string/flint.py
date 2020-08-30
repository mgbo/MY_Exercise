# -*- coding: utf-8 -*-

x=0
y=0

while True:
	line=raw_input()
	
	if line == 'Treasure!':
		print x,y
		break
	
		
	pair=line.split()
	direction = (pair[0])
	d = int(pair[1])
	
	if direction == 'North':
		y=y+d
		#print x,y
		#continue
		
	if direction == 'South':
		y=y-d
		#print x,y
		#continue
		
	if direction == 'East':
		x=x+d
		#print x,y
		#continue
		
	if direction == 'West':
		x=x-d
		#print x,y
		#continue
	
