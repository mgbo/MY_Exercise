#-*- coding:utf-8-*-
import turtle
import time
import math

def write(data):
	t.write(data, font=("Arial",14,"normal"))
	
def rect(size,col):
	t.color(col)
	for i in range(4):
		t.fd(size)
		t.lt(90)

def carre(size,col):
	t.color(col)
	rect(size,col)
	bedro = size/2
	r = math.sqrt(bedro*bedro+bedro*bedro)
	return r

t=turtle.Turtle()
t.shape('turtle')
t.width(3)

p = t.pos()
r = carre(200,'red')
t.rt(45)
t.circle(r)


turtle.done()
