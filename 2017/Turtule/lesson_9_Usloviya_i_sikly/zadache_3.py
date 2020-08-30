

# -*- coding: utf-8 -*-
import turtle           
import time

def write(data):
    t.write(data, font=("Arial", 14, "normal"))

def rect(size):
	for j in range(4):
		t.fd(size)
		t.lt(90)

t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(0)
col=['red','yellow']



for i in range(2):
	p = t.pos()
	for j in range(5):
		t.color(col[i%2],col[i%2])
		t.begin_fill()
		rect(50)
		t.fd(50)
		t.end_fill()
	t.goto(p)
	t.seth(90)
	t.fd(50)
	t.rt(90)


turtle.done()
