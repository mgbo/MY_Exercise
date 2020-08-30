
# -*- coding: utf-8 -*-

import turtle
from time import sleep

t = turtle.Turtle()

def line(x1,y1,x2,y2):
	t.up()
	t.goto(x1,y1)
	t.down()
	t.goto(x2,y2)

def sqb(x1,y1,x2,y2):
	t.color("red","blue")
	t.begin_fill()
	line(x1,y1,x2,y1)
	line(x2,y1,x2,y2)
	line(x2,y2,x1,y2)
	line(x1,y2,x1,y1)
	t.end_fill()
	t.up()
	t.goto(x2,y2)
	t.down()


'''
sqb(0,40,40,0)
sleep(2)
sqb(80,40,120,0)
'''
x = 0
y = 0
i = 0

while i<=5:
	sleep(1)
	sqb(0+x,40,40+y,0)
	t.fd(40)
	x+=80
	x+=80
	i+=1


turtle.done()
