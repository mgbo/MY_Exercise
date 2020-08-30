#-*- coding:utf-8-*-

import turtle
from time import sleep
import math 

t=turtle.Turtle()

def carre(size,col):
	t.color('blue',col)
	t.begin_fill()
	for i in range(4):
		t.fd(size)
		t.lt(90)
	t.end_fill()

def carre2(size1,size2,col1,col2):
	if col1==col2:
		if col1=="red":
			col2="yellow"
		else:
			col2="red"
	carre(size1,col1)
	carre(size2,col2)

carre2(200,100,"yellow","yellow")

turtle.done()
