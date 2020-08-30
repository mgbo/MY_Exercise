
# -*- coding: utf-8 -*-
import turtle
from time import sleep
import math 

def write(data):
	t.write(data, font=("Arial",14,"normal"))
	
def tri (p1,p2,p3,col):
	t.up()
	t.goto(p1)
	t.down()
	t.color(col)
	t.begin_fill()
	t.goto(p2)
	t.goto(p3)
	t.end_fill()

def rect(w,h):
	po = t.pos()
	write(po)
	print ("Po : ", po)
	a = w/2
	b = h/2

	t.fd(a)
	t.rt(90)
	t.fd(b)
	t.rt(90)

	prb = t.pos()
	write(prb)
	print ("prt : ", prb)
	t.fd(w)
	t.rt(90)

	plb = t.pos()
	write(plb)
	print ("plb : ",plb)
	t.fd(h)
	t.rt(90)

	plt = t.pos()
	write(plt)
	print ("plt : ",plt)
	t.fd(w)
	t.rt(90)

	prt = t.pos()
	write(plt)
	print ("plt : ",prt)
	t.fd(h)
	t.rt(90)

	tri(po,plt,prt,"darkgreen")
	tri(po,prt,prb,"blue")
	tri(po,plb,plt,"red")
	tri(po,plb,prb,"yellow")

t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(1)
#tri((0,0),(200,0),(0,100),"darkgreen")
rect(400,300)

turtle.done()
