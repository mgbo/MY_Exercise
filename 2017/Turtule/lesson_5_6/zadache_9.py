
# -*- coding: utf-8 -*-

import turtle
import time

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

def spi2(size,d,ang):
	p = t.pos()
	ang0 = t.heading()
	spi(size,d,ang)
	t.up()
	t.goto(p)
	time.sleep(3)
	t.down()
	time.sleep(3)
	spi(size,d,-ang)


t=turtle.Turtle()
t.width(3)
t.shape('turtle')
t.color('red')
t.speed(1)
spi2(80,20,90)

turtle.done()
