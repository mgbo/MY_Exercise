# -*- coding: utf-8 -*-
import turtle
import time

def ray(size,n):
	sizeOfRay = size/5*n
	t.seth(-45)
	for _ in range(n/2):
		t.fd(sizeOfRay)
		t.bk(sizeOfRay)
		t.lt(45)
	sizeOfRay*=2
	t.seth(0)
	t.bk(sizeOfRay)
	t.seth(-45)
	for _ in range(n/2):
		t.fd(sizeOfRay)
		t.bk(sizeOfRay)
		t.lt(45)
	t.seth(0)
	t.bk(size)

def snee(size,n):
	for _ in range(n):
		t.down()
		ray(size,n)
		t.lt(360/n)
		t.up()

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
t.speed(1)

#ray(15,6)
#snow(10,2)
snee(20,6)
#pattern(10,10)
#t.hideturtle()
turtle.done()

