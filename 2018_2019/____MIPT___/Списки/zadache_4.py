

import turtle
import sys

fb = ('Arial', 14, 'normal')
fp = sys.stdin

t = turtle.Turtle()
t.color('blue')


t.pu()
point = []
for string in fp:
	x, y = map(int, string.split())
	point.append((x,y))
	print (x, y)
	t.setpos(x, y)
	t.write((x,y), font= fb)
	t.pd()

t.setpos(point[0])

turtle.done()


