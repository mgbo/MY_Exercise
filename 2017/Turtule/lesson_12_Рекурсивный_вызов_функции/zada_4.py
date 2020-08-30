
# -*- coding: utf-8 -*-
import turtle           
import time
import math

def col_change(col):
	t.color(col)
	if col=='red':
		col='gold'
	elif col=='gold':
		col='blue'
	elif col=='blue':
		col='red'
	return col
	
def spi(size,d,n,col):
	if size<30:
		return
	if n<0:
		return
	col_change(col)
	t.fd(size)
	t.lt(90)
	col=spi(size-d,d,n-1,col)

t = turtle.Turtle()
t.shape("turtle")
t.width(3)

spi(200,10,15,'red')
turtle.done()
