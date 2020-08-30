
# -*- coding: utf-8 -*-
import turtle           
import time

def write(data):
	t.write(data,font = ("Arial",14,"normal"))

def spiral2(n,start_size,delta):
	t.color("red")
	t.seth(270)
	t.fd(start_size)
	for i in range(n):
		t.rt(90)
		t.fd(start_size)
		start_size+=delta
	write(start_size)
	
	t.color("blue")
	t.seth(0)
	t.fd(start_size)
	#write(start_size)
	start_size-=delta
	for i in range(n):
		t.rt(90)
		start_size-=delta
		t.fd(start_size)
		
	
t = turtle.Turtle()
t.shape("turtle")
t.color('green')
t.width(2)

spiral2(19,20,10)
t.hideturtle()
turtle.done()
