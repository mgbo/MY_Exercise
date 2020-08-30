
#-*- coding:utf-8-*-
import turtle
import time

t=turtle.Turtle()
t.shape('turtle')

def cir(r):
	t.color('blue')
	t.width(width=5)
	t.circle(r,None,None)
	cent = r
	t.up()
	t.goto(0,cent)
	t.down()

cir(120)
turtle.done()
