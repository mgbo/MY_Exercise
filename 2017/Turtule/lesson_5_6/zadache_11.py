
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

def spi1(size,d,ang):
	p = t.pos()
	spi(size,d,ang)
	t.up()
	t.goto(p)
	t.down()
	t.seth(180)
	spi(size,d,-ang)

def spi2(size,d,ang):
	p1 = t.pos()
	write(p1)
	spi1(size,d,ang)
	t.up()
	t.goto(size,d-size)
	p2 = t.pos()
	write(p2)
	t.seth(0)
	t.fd(2*size+size/2)
	t.down()
	spi1(size,d,-ang)
	p3 = t.pos()

	t.up()





t=turtle.Turtle()
t.width(3)
t.shape('turtle')
t.color('red')
spi1(100,20,90)

turtle.done()