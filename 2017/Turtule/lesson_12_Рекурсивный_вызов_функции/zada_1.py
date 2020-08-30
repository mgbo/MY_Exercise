
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

def sqn(size,d,n,i):
	if size<0:
		return
	if n==0:
		return
	sq(size,hues[i%6])
	goto_next(d/2)
	sqn(size-d,d,n-1,i+1)

t = turtle.Turtle()
t.shape("turtle")
t.width(3)

sqn(100,20,7,0)

turtle.done()












