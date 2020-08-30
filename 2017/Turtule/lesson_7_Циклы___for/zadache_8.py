
# -*- coding: utf-8 -*-
import turtle
import time
import math

def write(data):
	t.write(data, font=("Arial",14,"normal"))

def carre(size,col1,col2):
	t.color('blue',col1)
	t.begin_fill()
	for i in range(4):  
		t.fd(size)
		t.lt(90)
	t.end_fill()
	t.rt(90)
	t.bk(size/2)
	t.lt(45)

	t.color('red',col2)
	t.begin_fill()
	size=size/math.sqrt(2)
	for i in range(4):
		t.fd(size)
		t.lt(90)
	t.end_fill()
	t.rt(90)
	t.bk(size/2)
	t.lt(45)

def carreIncarre(size,n):
	for _ in range(n):
		carre(size,'darkgreen','yellow')
		size/=2

t = turtle.Turtle()
t.shape('turtle')
t.width(2)

#carre(100,'darkgreen','yellow')
carreIncarre(200,4)

t.hideturtle()
turtle.done()
