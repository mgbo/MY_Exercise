# -*- coding: utf-8 -*-
import turtle           
import time

def rect(size):
	for j in range(4):
		t.fd(size)
		t.lt(90)

def docka(v,h):
	for i in range(v):
		p = t.pos()
		for j in range(h):
			if i%2==0:
				t.color('blue',col1[j%2])
			else:
				t.color('blue',col2[j%2])
			t.begin_fill()
			rect(50)
			t.fd(50)
			t.end_fill()
		t.goto(p)
		t.seth(90)
		t.fd(50)
		t.rt(90)

t = turtle.Turtle()
t.width(3)
t.speed(0)
col1=['red','yellow']
col2=['yellow','red']

docka(5,5)

turtle.done()
