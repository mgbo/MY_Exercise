
#-*- coding:utf-8-*-
import turtle
import time

def write(data):
	t.write(data,font = ("Arial",30,"normal"))

def circR(r,color):
	p0 = t.pos()
	t.color(color)
	t.width(width=5)
	t.circle(r,None,None)
	t.up()
	t.goto(0,r)
	cen = t.pos()
	t.goto(p0)
	return cen

t=turtle.Turtle()
t.shape('turtle')

CirC = circR(120,'blue')
t.goto(CirC)
t.write("Центре окружности")

turtle.done()
