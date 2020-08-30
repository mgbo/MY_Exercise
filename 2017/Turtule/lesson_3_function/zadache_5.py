
# -*- coding: utf-8 -*-

import turtle
from time import sleep

t=turtle.Turtle()
t.width(3)
t.speed('fastest')

def snow():
	t.color("blue")
	t.fd(100)
	t.lt(45)
	for _ in range(3):
		t.fd(50)
		t.bk(50)
		t.rt(45)
	t.lt(90)
	t.bk(100)



for _ in range(6):
	snow()
	t.lt(60)

turtle.done()
