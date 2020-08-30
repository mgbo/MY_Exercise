# -*- coding: utf-8 -*-
import turtle           
import time

def write(data):
    t.write(data, font=("Arial", 14, "normal"))

def rect(size):
	for j in range(4):
		t.fd(size)
		t.lt(90)

def csq_hrect(size,rows,cols):
	col=['red','yellow']
	for i in range (rows):
		p = t.pos()
		for j in range(cols):
			t.color('blue',col[i%2])
			t.begin_fill()
			rect(size/rows)
			t.fd(size/rows)
			t.end_fill()
		t.goto(p)
		t.seth(90)
		t.fd(size/rows)
		t.rt(90)

t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(0)

csq_hrect(500,5,5)

turtle.done()