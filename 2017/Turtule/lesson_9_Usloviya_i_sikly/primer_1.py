# -*- coding: utf-8 -*-
import turtle           
import time

def write(data):
    t.write(data, font=("Arial", 14, "normal"))


t = turtle.Turtle()
t.shape("turtle")
t.width(3)

for i in range(5):
	if i==0 or i ==3:
		col='red'
	else:
		col='blue'
	t.color(col)
	write(i)
	t.fd(50)

turtle.done()
