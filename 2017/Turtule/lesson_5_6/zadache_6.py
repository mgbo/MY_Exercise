
# -*- coding: utf-8 -*-

import turtle
import time

def write(data):
	t.write(data, font=("Arial",14,"normal"))

def spi(size,d):
	t.down()
	t.color("blue")
	write(size)
	t.fd(size)
	t.rt(90)
	t.fd(size)
	t.rt(90)
	t.color("darkgreen")
	size += d
	t.fd(size)
	t.rt(90)
	t.fd(size)
	t.rt(90)
	t.color("red")
	size += d
	t.fd(size)
	t.rt(90)
	t.fd(size)
	t.rt(90)
	t.color('darkorange')
	size += d
	t.fd(size)
	t.rt(90)
	t.fd(size)
	t.rt(90)
	t.color('yellow')
	size += d
	t.fd(size)
	

t = turtle.Turtle()
t.shape("turtle")
t.width(5)

spi(70,40)
turtle.done()












