
# -*- coding: utf-8 -*-

import turtle
from time import sleep

t=turtle.Turtle()
t.width(3)
t.speed('fastest')

def snow(x1,x2):
	t.color("blue")
	t.fd(x1)
	t.lt(45)
	for _ in range(3):
		t.fd(x2)
		t.bk(x2)
		t.rt(45)
	t.lt(90)
	t.bk(x1)



for _ in range(6):
	snow(100,50)
	t.lt(60)
t.up()
t.goto(-300,0)
t.down()
for _ in range(6):
	snow(50,25)
	t.lt(60)
turtle.done()
