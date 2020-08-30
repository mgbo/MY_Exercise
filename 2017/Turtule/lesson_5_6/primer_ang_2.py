
# -*- coding:utf-8 -*-

import turtle
import time

def write(data):
	t.write(data, font=("Arial",14,"normal"))

def lines(size):
	#t.down()
	t.color("blue")
	write(500)
	t.fd(size)

	size+=50 # увеличили size на 50

	t.color("darkgreen")
	write(size)
	t.fd(size)

	size+=50
	
	t.fd(size)
	tp = t.pos()
	write(tp)


	x = t.xcor()
	y = t.ycor()
	print (x,y)


t = turtle.Turtle()
t.shape("turtle")
t.width(3)
lines (100)

turtle.done()







