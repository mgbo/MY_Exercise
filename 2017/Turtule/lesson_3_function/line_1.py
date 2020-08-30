
# -*- coding: utf-8 -*-
import turtle         
from time import sleep 
import math

def xy():
	x,y = t.pos()
	x = int(x)
	y = int(y)
	t.write((x,y), font = ("Arial", 14,"normal"))

def line(x1,y1,x2,y2,col,wid):
	t.color(col)
	t.width(wid)
	t.penup()
	t.goto(x1,y1)
	xy()
	
	t.pendown()
	t.goto(x2,y2)
	xy()
	
t = turtle.Turtle()
t.shape("turtle")

line(-200,50,100,-50,'red',5)

t.hideturtle()
turtle.mainloop()
