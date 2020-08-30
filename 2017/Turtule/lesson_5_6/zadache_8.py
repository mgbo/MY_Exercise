
# -*- coding: utf-8 -*-
import turtle
import time
import math

def write(data):
	t.write(data, font=("Arial",14,"normal"))

def sq(size,ang,col1,col2):
	t.color(col1,col2)
	t.begin_fill()
	t.fd(size)
	t.lt(ang)
	t.fd(size)
	t.lt(ang)
	t.fd(size)
	t.lt(ang)
	t.fd(size)
	t.end_fill()
	t.bk(size/2)

def sq3(size,ang):
	sq(size,ang,'blue','darkgreen')
	t.lt(45)
	sq(size/math.sqrt(2),ang,'red','yellow')
	t.lt(45)
	sq(size/math.sqrt(4),ang,'magenta','darkorange')

t = turtle.Turtle()
t.shape('turtle')
t.width(3)
sq3(200,90)
t.up()
t.goto(400,75)
t.rt(135)
t.down()
time.sleep(3)
#sq3(200,90)

turtle.hideturtle()


turtle.done()
