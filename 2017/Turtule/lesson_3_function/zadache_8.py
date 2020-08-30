
# -*- coding: utf-8 -*-
import turtle
from time import sleep

def sq(col):
    t.color(col)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)

def tri(col):
	t.color(col)
	t.fd(100)
	t.lt(120)
	t.fd(100)
	t.lt(120)
	t.fd(100)

t = turtle.Turtle()
#t1 = turtle.Turtle()

t.shape("turtle")
t.width(3)

t.left(45)
sq("red")
t.seth(0)
sq("green")
sleep(3)

tri("darkgreen")

t.seth(180)
tri("magenta")

turtle.done()
