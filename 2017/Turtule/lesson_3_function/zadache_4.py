
# -*- coding: utf-8 -*-

import turtle
from time import sleep

t=turtle.Turtle()
t.width(3)

t.speed('slowest')

def cross():
	t.color("blue")
	t.fd(100)
	t.bk(200)
	t.fd(100)
	t.lt(90)
	t.fd(100)
	t.bk(200)
	t.fd(100)
	t.hideturtle()

cross()
t.seth(45)
cross()

turtle.mainloop()


