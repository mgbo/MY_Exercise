
# -*- coding: utf-8 -*-
import turtle           
import time

def write(data):
	t.write(data, font = ("Aria",14,"normal"))
	
def sqr(col2):
	t.color('black',col2)
	t.begin_fill()
	for _ in range(4):
		t.fd(50)
		t.lt(90)
	t.end_fill()

def polosa(n,col1,col2):
	x=50
	for _ in range(n):
		#p =t.pos()
		#write(p)
		sqr(col1)
		t.up()
		t.fd(x)
		t.down()
		sqr(col2)
		t.fd(x)
	t.up()
	t.fd(-(2*n*50))


t = turtle.Turtle()
t.shape("turtle")
t.width(3)
#sqr('red')
t.speed(0)
polosa(5,'red','yellow')
t.seth(90)
t.fd(50)
t.seth(0)
time.sleep(3)
polosa(5,'yellow','red')


turtle.done()
