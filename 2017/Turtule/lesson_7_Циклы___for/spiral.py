

# -*- coding: utf-8 -*-
import turtle           
import time

def write(data):
	t.write(data,font = ("Arial",14,"normal"))

def spirale(n):
	x = 20
	t.seth(270)
	for _ in range(n):
		t.fd(x)
		t.lt(90)
		x+=10
	
t = turtle.Turtle()
t.shape("turtle")
t.color('green')
t.width(2)

spirale(15)

turtle.done()