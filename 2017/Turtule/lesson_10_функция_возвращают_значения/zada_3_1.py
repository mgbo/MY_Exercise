#-*- coding:utf-8-*-
import turtle
import time
import math

def trC(size,color):
	t.color(color)
	p =t.pos()
	for i in range(3):
		t.fd(size)
		t.lt(120)
	t.lt(-120)
	t.bk(size/2)
	r = math.sqrt(3)*size/6
	return r

t=turtle.Turtle()
t.shape('turtle')
t.width(3)

r = trC(250,'blue')
t.circle(r)
turtle.done()
