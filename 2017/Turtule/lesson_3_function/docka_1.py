# -*- coding: utf-8 -*-
import turtle         
from time import sleep 
import math

def xy():
	x,y = t.pos()
	x = int(x)
	y = int(y)
	t.write((x,y), font=("Arial",14,"normal"))
	
def line(x1,y1,x2,y2):
	t.penup()
	t.goto(x1,y1)
	xy()
	
	t.pendown()
	t.goto(x2,y2)
	xy()

def rect(x1,y1,x2,y2,col,col2):
	t.color(col,col2)
	
	t.begin_fill()
	line(x1,y1,x2,y1)
	line(x2,y1,x2,y2)
	line(x2,y2,x1,y2)
	line(x1,y2,x1,y1)
	t.end_fill()
	
t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed('slowest')
#line(-10,150,200,150)

rect(-10,150,200,-20,"red","darkgreen")
p = t.pos()
print (p)

t.penup()
t.goto(100,30)
t.pendown()

i=0
t.color('white')
'''
while i<=32:
	t.lt(11.25)
	t.fd(10)
	i+=1
'''
while i<=2:
	t.fd(50)
	t.lt(120)
	i+=1
	
t.hideturtle()
turtle.done()
