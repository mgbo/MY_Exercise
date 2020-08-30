
# -*- coding: utf-8 -*-

import turtle
from time import sleep

def write(data):
	t.write(data, font=("Arial",14,"normal"))

def line(p11,p22):
	t.color("red")
	t.up()
	t.goto(p11)
	t.down()
	#write(p11)

	t.goto(p22)
	#write(p22)

def uzor(w,h,ang):
	t.seth(ang)
	b0 = t.pos()
	step = w/5	

	t.fd(step)
	b1 = t.pos()

	t.up()
	t.fd(step)
	b2 = t.pos()

	t.down()
	t.fd(step)
	b3 = t.pos()

	t.up()
	t.fd(step)
	b4 = t.pos()

	t.down()
	t.fd(step)
	b5 = t.pos()

	t.up()
	t.goto(b0)
	t.lt(90)
	t.fd(h)
	t.rt(90)
	t0 = t.pos()

	t.down()
	t.fd(step)
	t1 = t.pos()

	t.up()
	t.fd(step)
	t2 = t.pos()

	t.down()
	t.fd(step)
	t3 = t.pos()

	t.up()
	t.fd(step)
	t4 = t.pos()

	t.down()
	t.fd(step)
	t5 = t.pos()

	line(b2,t0)
	line(b3,t1)
	line(b4,t2)
	line(b5,t3)

	line(b0,t2)
	line(b1,t3)
	line(b2,t4)
	line(b3,t5)

	

t = turtle.Turtle()
t.shape("turtle")
t.color("red")
t.width(3)

uzor(100,50,0)
turtle.done()




