
# -*- coding: utf-8 -*-
import turtle           
import time
import math

hues = [
  'violet',   # hues[0]
  'blue',     # hues[1]
  'green',    # hues[2]
  'yellow',   # hues[3]
  'gold',     # hues[4]
  'orange',   # hues[5]
  'red'       # hues[6]
  ]

def sq(size,k,col):  # нарисовать квадрат размера size цвета col
  t.color(col)
  for i in range(k):
    t.fd(size)
    t.left(360/k)

def move(size,k):
	t.up()
	t.rt(360/k)
	t.fd(-size/2)
	t.lt((360/k)/2)
	t.down()

def sqn(size,k,n,i):
	if size<30:
		return
	if n==0:
		return
	sq(size,k,hues[i%6])
	move(size,k)
	sqn(math.sqrt((2*(size/2)**2-(2*(size/2)*(size/2))*(math.cos(360/(2*k))))),k,n-1,i+1)

t = turtle.Turtle()
t.shape("turtle")
t.width(3)

#sq(100,5,'red')
#move(100,5)
sqn(200,5,7,0)
turtle.done()
