
# -*- coding: utf-8 -*-
import turtle           
import time

def write(data):
    t.write(data, font=("Arial", 14, "normal"))

def circle(r):
	for i in range(32):
		t.fd(r)
		t.lt(360/32)

def circR(radius,color):
	circle(radius)

	xc = radius/2
	yc = radius/2



t = turtle.Turtle()
t.shape("turtle")
t.width(3)

circR(20,'blue')
turtle.done()
