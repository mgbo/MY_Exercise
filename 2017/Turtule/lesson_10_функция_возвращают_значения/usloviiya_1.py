
#-*- coding:utf-8-*-
import turtle
import time
import math

def write(data):
	t.write(data,font = ("Arial",14,"normal"))

def carre(size,col):
	t.down()
	t.color(col)
	if size ==0:
		write("не буду рисовать")
		return t.pos()
	elif size == 200:
		write("Очень большой")

	elif 0<size and size <200:
		write("правильный")
	else:
		write("плохиие размеры")

	for n in range(4):
		t.fd(size)
		t.left(90)

t=turtle.Turtle()
t.shape('turtle')
wn = turtle.Screen()
t.width(3)

kartina = carre(250,'blue')

wn.exitonclick()