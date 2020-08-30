
# -*- coding: utf-8 -*-

import turtle
from time import sleep

t=turtle.Turtle()
t.width(3)

def sq():
	t.color("red","yellow")
	t.begin_fill()
	
	t.fd(100)
	sleep(1)
	t.lt(90)
	sleep(1)
	t.fd(100)
	t.lt(90)
	sleep(1)
	t.fd(100)
	sleep(1)
	t.lt(90)
	sleep(1)
	t.fd(100)
	sleep(1)
	
	t.end_fill()

sq()
t.seth(45)
sq()
t.seth(90)
sq()

turtle.mainloop()
