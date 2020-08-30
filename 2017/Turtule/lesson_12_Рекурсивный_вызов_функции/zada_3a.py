
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

def tri(size, col):  # нарисовать квадрат размера size цвета col
  t.color(col)
  for i in range(3):
    t.fd(size)
    t.left(120)

def move(size):
	t.rt(120)
	t.fd(-size)
	t.lt(60)

def mnogo_tri(size,n,i):
	if n<0:
		return
	if size<20:
		return
	tri(size,hues[i%6])
	move(size/2)
	mnogo_tri(size/2,n-1,i+1)


t = turtle.Turtle()
t.shape("turtle")
t.width(3)

mnogo_tri(200,7,0)

turtle.done()


