
# -*- coding: utf-8 -*-
import turtle
import time

t=turtle.Turtle()
t.color("blue")
t.width(2)
#t.speed('fastest')

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

snow(25,3)




turtle.done()

