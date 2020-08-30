# -*- coding: utf-8 -*-
import turtle           
import time
	
def sqr(col2,ang):
	x=25
	t.seth(0)
	t.color('black',col2)
	t.begin_fill()
	for _ in range(4):
		t.fd(x)
		t.lt(ang)
	t.end_fill()

def polosa(n):
	x=25
	for _ in range(n):
		sqr('red',90)
		t.fd(x)
		t.down()
		sqr('yellow',90)
		t.fd(x)
	for _ in range(n):
		t.bk(x)
		sqr('red',-90)
		t.bk(x)
		sqr('yellow',-90)

def chess(n,m):
	x = 25
	for i in range(m):
		t.down()
		polosa(n)
		t.rt(90)
		t.up()
		t.fd(2*x)

t = turtle.Turtle()
t.shape("turtle")
t.width(2)
t.speed(0)
chess(5,5)
turtle.done()
