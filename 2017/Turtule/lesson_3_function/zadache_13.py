
# -*- coding: utf-8 -*-

import turtle
from time import sleep
import math

t = turtle.Turtle()

def sqr(x,col1):
	t.color(col1)
	t.fd(x)
	t.lt(90)
	t.fd(x)
	t.lt(90)
	t.fd(x)
	t.lt(90)
	t.fd(x)
	t.bk(x/2)
	

def sqr2(x,col1,col2,wid):
	t.width(wid)
	sqr(x,col1)
	t.lt(45)
	sqr(x/math.sqrt(2),col2)


sqr2(200,"red","blue",3)
t.hideturtle()
turtle.done()
