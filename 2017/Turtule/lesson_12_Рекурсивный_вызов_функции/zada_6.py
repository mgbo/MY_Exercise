
# -*- coding: utf-8 -*-
import turtle
import time
import math

def branch(n, size0, dsize, ang0, dang):
	size=size0
	ang=ang0
	for i in range(n):
		if i==n/2:
			p = t.pos()
		t.fd(size)
		t.lt(ang)
		size-=dsize
		ang+=dang
	return p

def uzor(n,size0,dsize,ang0,dang,k):
	if k==0:
		return
	p0 = branch(6,50,5,10,15)
	t.up()
	t.goto(p0)
	t.down()
	t.seth(0)
	uzor(n,size0,dsize,-ang0,-dang,k-1)

t = turtle.Turtle()
t.shape('turtle')
t.width(3)

uzor(6,20,5,10,15,3)

turtle.done()
