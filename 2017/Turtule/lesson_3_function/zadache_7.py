
# -*- coding: utf-8 -*-

import turtle
from time import sleep

t = turtle.Turtle()


def peak():
	t.color("blue")
	t.lt(60)
	t.fd(100)
	t.rt(120)
	t.fd(100)

def peak2():
	
	peak()
	sleep(3)
	t.seth(0)
	peak()
	t.seth(0)
	peak()
	
peak2()

turtle.done()

