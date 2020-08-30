
# -*- coding: utf-8 -*-
import turtle           
import time

hues = [
  'violet',   # hues[0]
  'blue',     # hues[1]
  'green',    # hues[2]
  'yellow',   # hues[3]
  'gold',     # hues[4]
  'orange',   # hues[5]
  'red'       # hues[6]
  ]

def sq(size, col):  # нарисовать квадрат размера size цвета col
  t.color(col)
  for i in range(4):
    t.fd(size)
    t.left(90)

def goto_next(d):
	t.up()
	t.fd(d)
	t.lt(90)
	t.fd(d)
	t.right(90)
	t.down()

def sqn(size,d,n):
	for i in range(n):
		sq(size,hues[i])
		size-=d
		if size<0:
			return 
		goto_next(d/2)

t = turtle.Turtle()
t.shape("turtle")
t.width(3)

sqn(200,20,7)

turtle.done()












