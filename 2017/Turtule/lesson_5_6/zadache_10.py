
# -*- coding:utf-8 -*-

import turtle
import time

def write(data):
	t.write(data, font = ("Arial",14,"normal"))

def spi(size,d,ang):
	t.fd(size)
	t.rt(ang)

	size-=d
	t.fd(size)
	t.rt(ang)
	t.fd(size)

	t.rt(ang)
	size-=d
	t.fd(size)
	t.rt(ang)
	t.fd(size)

	size-=d
	t.rt(ang)
	t.fd(size)
	t.rt(ang)
	t.fd(size)

	t.rt(ang)
	size-=d
	t.fd(size)

def spi2(size,d,ang):
	p = t.pos()
	ang0 = t.heading()
	spi(size,d,ang)
	t.up()
	t.goto(p)
	t.down()
	time.sleep(5)
	t.seth(180)
	spi(size,d,-ang)

t=turtle.Turtle()
t.width(3)
t.shape('turtle')
t.color('red')
t.speed(1)
spi2(100,20,90)
t.up()
t.goto(300,-80)
t.down()
t.seth(0)
spi2(100,20,-90)

turtle.done()