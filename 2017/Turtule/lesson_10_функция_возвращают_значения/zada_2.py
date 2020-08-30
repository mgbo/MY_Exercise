
#-*- coding:utf-8-*-
import turtle
import time
import math

t=turtle.Turtle()
t.shape('turtle')
t.width(3)

def trC(size,color):
	t.color(color)
	for i in range(3):
		t.fd(size)
		t.lt(120)
		
	p = (3*size)/2
	s = math.sqrt(p*((p-size)*(p-size)*(p-size)))
	r = (2*s)/(3*size)
	print ("Radius : ",r)
	
	t.up()
	t.goto(size/2,r)
	pc = t.pos()
	t.goto(0,0)
	return pc

p = trC(150,'blue')
t.goto(p)

turtle.done()
