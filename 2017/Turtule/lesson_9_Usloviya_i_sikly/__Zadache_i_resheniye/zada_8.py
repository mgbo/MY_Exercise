# -*- coding: utf-8 -*-
import turtle           
import time

def rect(size):
	for j in range(4):
		t.fd(size)
		t.lt(90)

def csq_3(size,n):
	col=['red','yellow']
	for j in range(n):
		t.color('gold',col[j%2])
		t.begin_fill()
		rect(size)
		t.end_fill()
		t.fd(size)

def serial(size,n):
	while n>0:
		csq_3(size,n)
		t.lt(90)
		t.fd(size)
		n-=1

t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(0)

serial(50,5)

turtle.done()
