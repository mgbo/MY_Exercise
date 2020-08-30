#-*- coding:utf-8-*-
import turtle
import time
import math

def write(data):
	t.write(data,font=('Arial',14,"normal"))

def line(x):
	t.stamp()
	t.up()
	t.setx(x)
	t.lt(90)
	t.down()
	t.fd(300)
	t.fd(-600)
	t.right(90)

def circRight(centr,radius,x):
	line(x)
	if x<=centr - radius:
		t.up()
		t.goto(centr,0)
		t.stamp()
		t.goto(centr,-radius)
		t.down()
		
		t.circle(radius)
	else:
		t.up()
		t.goto(centr,0)
		t.stamp()
		t.goto(centr,-radius)
		t.down()
		
		t.circle(radius)
		write("Плохо")


t=turtle.Turtle()
t.width(3)
t.shape('turtle')
t.speed(3)

t.color('blue')
circRight(300,70,100)
turtle.done()
