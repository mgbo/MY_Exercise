
# -*- coding: utf-8 -*-
import turtle           
import time

def rect(size):
	for j in range(4):
		t.fd(size)
		t.lt(90)

def csq_chess(size,rows,cols):
	col=['red','yellow']
	col1=['yellow','red']
	for i in range (rows):
		p = t.pos()
		for j in range(cols):
			if i%2==0:
				t.color('blue',col[j%2])
			else:
				t.color('blue',col1[j%2])
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

csq_chess(300,3,3)
turtle.done()


