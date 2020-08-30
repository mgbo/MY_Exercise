
import turtle
import time
import math

def ks(length,d):
	if d==0:
		t.fd(length)
	else:
		length=length/3
		d=d-1
		ks(length,d)
		t.right(60)
		ks(length,d)
		t.left(120)
		ks(length,d)
		t.right(60)
		ks(length,d)

t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(0)

#ks(300,3)
#t.update()
#t.reset()

colors = ["red","orange","pink"]
for i in range(3):
	t.color(colors[i])
	ks(300,2)
	t.left(120)

turtle.done()


