
# -*- coding: utf-8 -*-

import turtle
from time import sleep

t=turtle.Turtle()
t.shape("turtle")
t.width(3)

def leaf():
	t.color("darkgreen")
	t.begin_fill()
	
	t.forward(150)
	#sleep(1)
	t.rt(45)
	
	t.fd(150)
	t.rt(135)
	
	t.fd(150)
	t.rt(45)
	
	t.fd(150)
	t.end_fill()
	
leaf()
sleep(1)
t.seth(90)

sleep(1)
leaf()

sleep(1)
t.seth(180)
leaf()

t.hideturtle()
turtle.done()
