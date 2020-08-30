
# -*- coding: utf-8 -*-
import turtle
import time
import math

def fib0(size):
	for i in range(4):
		t.fd(size)
		t.lt(90)

def sq_fo(n):
	if n<2:
		return n
	else:
		return sq_fo(n-1) + sq_fo(n-2)
		

t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(1)

ans = sq_fo(5)
print (ans)


turtle.done()    

	
