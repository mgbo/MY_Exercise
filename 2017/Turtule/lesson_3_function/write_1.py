
# -*- coding: utf-8 -*-

import turtle         
from time import sleep 
import math

def xy():
	x,y = t.pos()
	x = int(x)
	y = int(y)
	t.write((x,y), font=("Arial",14,"normal"))
	
def line(x1,x2):
	t.penup()
	t.goto(x1,0)
	t.color("blue")
	xy()
	
	t.color("blue")
	t.pendown()
	t.goto(x2,0)
	xy()

t = turtle.Turtle()
t.shape("turtle")
t.width(3)
'''
x1 = int(input("x1 = "))
x2 = int(input("x2 = "))
'''
line(-10,200)
t.hideturtle()
turtle.done()
