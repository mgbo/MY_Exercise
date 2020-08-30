
# -*- coding: utf-8 -*-
import turtle           
import time

def write(data):
    t.write(data, font=("Arial", 14, "normal"))

def csq(size,col):
	t.pencolor(col)
	t.begin_fill()
	for j in range(4):
		t.color(col)
		t.fd(size)
		t.lt(90)
	t.end_fill()

def csq_row(size,n,col1):
	p = t.pos()
	for i in range(n):
		if i%2 == 0:
			col1='red'
		else:
			col1='yellow'
		csq(size,col1)
		t.fd(size)
	t.up()
	t.goto(p)

t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(0)
csq_row(50,5,'red')

turtle.done()



