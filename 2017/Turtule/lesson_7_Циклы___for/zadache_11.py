# -*- coding: utf-8 -*-
import turtle
import time

def snow(size,n):
	t.fd(size)
	t.lt(45)
	sizeOfRay = size/3*n
	for _ in range(n):
		t.fd(sizeOfRay)
		t.bk(sizeOfRay)
		t.rt(45)
	t.lt(90)
	t.bk(size)

def snee(size,n):
	for _ in range(n):
		snow(size,3)
		t.lt(360/n)

def pattern (size,n):
	for _ in range(n):
		t.up()
		t.fd(5*size)
		t.down()
		snee(size,n)
		t.up()
		t.bk(5*size)
		t.lt(360/n)
	t.down()
	t.seth(0)
	snee(size,n)

t=turtle.Turtle()
t.color("blue")
t.width(2)
t.speed('fastest')

pattern(20,10)
t.hideturtle()
turtle.done()

