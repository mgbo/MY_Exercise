
# -*- coding: utf-8 -*-

import turtle
import time

def write(data):
	t.write(data, font=("Arial",14,"normal"))

def sun(r,size,angle,col):
	t.color(col)

	t.seth(angle)
	print angle
	t.up()
	t.fd(r)
	t.down()
	t.fd(size)
	t.up()
	t.bk(size+r)
	
	angle+=36
	print angle
	t.seth(angle)
	print angle
	t.up()
	t.fd(r)
	t.down()
	t.fd(size)
	t.up()
	t.bk(size+r)

	angle+=36
	t.seth(angle)
	t.up()
	t.fd(r)
	t.down()
	t.fd(size)
	t.up()
	t.bk(size+r)

	angle+=36
	t.seth(angle)
	t.up()
	t.fd(r)
	t.down()
	t.fd(size)
	t.up()
	t.bk(size+r)

	angle+=36
	t.seth(angle)
	t.up()
	t.fd(r)
	t.down()
	t.fd(size)
	t.up()
	t.bk(size+r)

	angle+=36
	t.seth(angle)
	t.up()
	t.fd(r)
	t.down()
	t.fd(size)
	t.up()
	t.bk(size+r)

	angle+=36
	t.seth(angle)
	t.up()
	t.fd(r)
	t.down()
	t.fd(size)
	t.up()
	t.bk(size+r)

	angle+=36
	t.seth(angle)
	t.up()
	t.fd(r)
	t.down()
	t.fd(size)
	t.up()
	t.bk(size+r)

	angle+=36
	t.seth(angle)
	t.up()
	t.fd(r)
	t.down()
	t.fd(size)
	t.up()
	t.bk(size+r)

	angle+=36
	t.seth(angle)
	print angle
	t.up()
	t.fd(r)
	t.down()
	t.fd(size)
	t.up()
	t.bk(size+r)

def sun2(r, size):
	sun(r, size, 0,'red')
	sun(r-10,size-20,12,'blue')
	sun(r-20,size-30,24,'darkgreen')

t = turtle.Turtle()
t.shape('turtle')
t.width(3)
t.speed(0)
sun2(50, 100)


turtle.done()


