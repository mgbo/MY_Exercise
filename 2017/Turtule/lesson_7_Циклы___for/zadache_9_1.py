
# -*- coding: utf-8 -*-
import turtle           
import time

def sqr(col2):
	t.seth(0)
	t.color('black',col2)
	t.begin_fill()
	for _ in range(4):
		t.fd(50)
		t.lt(90)
	t.end_fill()

def polosa(n):
	x=50
	for _ in range(n):
		sqr('red')
		t.up()
		t.fd(x)
		t.down()
		sqr('yellow')
		t.fd(x)
	t.up()
	t.bk(2*n*50)

def manyP(n,m):
	x = 50
	for i in range(m):
		t.down()
		polosa(n)
		t.seth(90)
		t.up()
		t.fd(x)
	
t = turtle.Turtle()
t.shape("turtle")
t.width(2)

#polosa(10)
manyP(3,5)
turtle.done()
