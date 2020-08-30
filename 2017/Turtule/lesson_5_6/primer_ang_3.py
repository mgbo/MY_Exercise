
# -*- coding:utf-8 -*-

import turtle
import time

def write (data):
	t.write(data, font = ("Arial",14,"normal"))

# size - длина первой линии
# d - на сколько будем изменять size

def lines(size,d):
	t.down()
	t.color("blue")
	write(size)
	t.fd(size)

	size += d
	t.color("red")
	write(size)
	t.fd(size)

	size += d

	t.color("gold")
	write(size)
	t.fd(size)

t = turtle.Turtle()
t.shape("turtle")
t.width(3)

t.up()
t.goto(-300,0)
p = t.pos()

lines(80,40)

time.sleep(3)

t.up()
t.goto(p)

t.seth(90)
t.fd(50)
t.seth(0)

lines(200,-40)

turtle.done()









