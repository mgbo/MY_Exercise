
# -*- coding: utf-8 -*-
import turtle           
import time

def rect(size):
	for j in range(4):
		t.fd(size)
		t.lt(90)

def csq_3(size,n):
	col=['red','yellow','darkgreen']
	p = t.pos()
	for j in range(n):
		t.color('gold',col[j%3])
		t.begin_fill()
		rect(size/n)
		t.end_fill()
		t.fd(size/n)
	t.goto(p)

t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(0)

csq_3(500,8)
turtle.done()


