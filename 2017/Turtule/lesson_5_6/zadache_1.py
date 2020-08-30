
# -*- coding: utf-8 -*-

import turtle
from time import sleep



def write(data):
	t.write(data, font=("Arial",14,"normal"))

def line(size):
	t.color("darkgreen")
	sleep(3)
	xy = t.pos()

	t.fd(size)
	sleep(3)
	t.color("yellow")
	t.fd(100)
	t.up()
	t.goto(xy)
	write(xy)

t = turtle.Turtle()
t.shape("turtle")
t.width(3)

t.goto(-200,0)
line(100)

turtle.done()
