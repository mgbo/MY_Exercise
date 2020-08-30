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

def sq(size,col):
	t.color(col)
	for i in range(4):
		t.fd(size)
		t.left(90)

def move(d):
	t.up()
	t.fd(d)
	t.down()

def sqn(size,n,i):
	if size<30:
		return
	if n==0:
		return
	sq(size,hues[i])
	move(size/(1+math.sqrt(3)))
	t.lt(30 )
	sqn(2*(size/(1+math.sqrt(3))),n-1,i+1)

t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(1)
sqn(200,7,0)

turtle.done()    
