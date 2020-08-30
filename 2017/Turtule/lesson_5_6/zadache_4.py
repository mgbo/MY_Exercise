
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
	t.rt(90)
	t.fd(h)
	t.lt(90)
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

	line(b0,t2)
	line(b1,t3)
	line(b2,t4)
	line(b3,t5)

	line(t0,b2)
	line(t1,b3)
	line(t2,b4)
	line(t3,b5)

def rectuzor(w,h):
	wstep = w/3
	hstep = h/2

	uzor(wstep,hstep,0)
	uzor(wstep,hstep,0)
	uzor(wstep,hstep,0)
	rbr = t.pos()
	t.up()
	t.lt(90)
	t.fd(hstep)
	print ("hstep : ", hstep)
	t.fd(h+hstep)
	print ("h : ", h)
	t.down()
	uzor(wstep,hstep,180)
	uzor(wstep,hstep,180)
	uzor(wstep,hstep,180)
	rtl = t. pos()
	write(rtl)

	uzor(wstep,hstep,270)
	uzor(wstep,hstep,270)
	rbl = t.pos()
	write(rbl)

	t.up()
	t.goto(rbr)
	t.down()
	write(rbr)
	uzor(wstep,hstep,90)
	uzor(wstep,hstep,90)
	rtr = t.pos()
	write(rtr)
	line(rtl,rbr)
	line(rtr,rbl)


t = turtle.Turtle()
t.shape("turtle")
t.color("red")
t.width(3)
t.speed(0)
rectuzor(300,100)
pt = t.pos()
print (pt)
turtle.done()




