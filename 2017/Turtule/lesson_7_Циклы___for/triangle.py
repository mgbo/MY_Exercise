
# -*- coding: utf-8 -*-
import turtle           
import time

def write(data):
	t.write(data,font = ("Arial",14,"normal"))

def triangle(size,cover):
	#a0 = t.heading()
	p0 = t.pos()
	t.fd(size)
	p1 = t.pos()
	t.fd(-size)

	t.rt(cover)
	t.fd(size)

	t.goto(p1)
	t.goto(p0)
	#t.seth(a0)

def Poligon(size,n):
	ang = 0
	for _ in range(n):
		t.seth(ang)
		triangle(size/2,360/n)
		#t.fd(size)
		ang += 360/n
		#time.sleep(2)
	
t = turtle.Turtle()
t.shape("turtle")
t.color('green')
t.width(2)

#t.seth(45)
triangle(100,90)

#Poligon(200,10)

turtle.done()
