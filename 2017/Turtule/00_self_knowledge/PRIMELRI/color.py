
# -*- coding: utf-8 -*-
import turtle
import time
import math

t = turtle.Turtle()

colors = ["blue","green","purple","cyan","magenta","violet"]

for i in range(45):
	t.color(colors[i%6]) 
	t.fd(5+i*3)
	t.lt(45)
	#t.width(i/45)
	#t.up()

turtle.done()
