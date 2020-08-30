
#-*- coding:utf-8 -*-

import turtle
import time

t=turtle.Turtle()
t.shape('turtle')
t.color('red')
t.stamp()
angle = 30

for i in range(12):
	t.up()
	t.fd(50)
	t.down()
	t.fd(25)
	t.up()
	t.stamp()
	t.home()
	t.rt(angle)
	angle+=30

turtle.done()
