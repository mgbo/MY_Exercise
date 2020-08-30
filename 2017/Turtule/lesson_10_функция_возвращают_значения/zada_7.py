
#-*- coding:utf-8 -*-
import turtle
import time

def dash(size,step):
	for i in range(step):
		if i%2==0:
			col='red'
		else:
			col='darkgreen'
		t.color(col)
		t.down()
		t.fd(50)
		t.up()
		t.fd(50)

t=turtle.Turtle()
t.shape('turtle')
t.width(3)

dash(20,10)
turtle.done()
