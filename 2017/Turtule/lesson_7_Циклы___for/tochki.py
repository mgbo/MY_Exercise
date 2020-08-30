
# -*- coding: utf-8 -*-
import turtle           
import time

def dash(n):
	for i in range(n):
		t.down()
		t.fd(n)
		t.up()
		t.fd(n)


t = turtle.Turtle()
t.shape("turtle")
t.color('green')
t.width(2)

t.color('red')
dash(15)
t.color('blue')
dash(15)

turtle.done()