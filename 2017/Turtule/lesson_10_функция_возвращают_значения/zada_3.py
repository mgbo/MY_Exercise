#-*- coding:utf-8-*-
import turtle
import time
import math

def circR(r,color):
	t.color(color)
	t.circle(r,None,None)

def trC(size,color):
	t.color(color)
	for i in range(3):
		t.fd(size)
		t.lt(120)
		
	p = (3*size)/2
	s = math.sqrt(p*((p-size)*(p-size)*(p-size)))
	r = (2*s)/(3*size)
	#print ("Radius : ",r)
	t.up()
	t.goto(size/2,0)
	t.down()
	circR(r,color)

t=turtle.Turtle()
t.shape('turtle')
t.width(3)

trC(250,'blue')
turtle.done()
