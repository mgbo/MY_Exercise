
# -*- coding: utf-8 -*-
import turtle           
import time

def sqr(col1,col2):
	t.color(col1,col2)
	t.begin_fill()
	for _ in range(4):
		t.fd(50)
		t.lt(90)
	t.end_fill()

t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.seth(0)
sqr('black','darkgreen')
turtle.done()
