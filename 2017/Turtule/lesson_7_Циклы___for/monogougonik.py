
# -*- coding: utf-8 -*-
import turtle           
import time

def write(data):
	t.write(data,font = ("Arial",14,"normal"))

def Poligon(n):
	for _ in range(n):
		t.fd(100)
		t.lt(360/n)

t = turtle.Turtle()
t.shape("turtle")
t.color('green')
t.width(2)

Poligon(8)


turtle.done()
