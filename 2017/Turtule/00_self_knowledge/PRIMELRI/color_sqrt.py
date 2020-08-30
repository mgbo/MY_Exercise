
import turtle
import time
import math

t = turtle.Turtle()

colors = ['blue','red','magenta','violet','purple','cyan','green']
#t.speed(0)

def sqr(col):
	t.color("blue",col)
	t.begin_fill()
	for i in range (4):
		t.fd(100)
		t.lt(90)
	t.end_fill()

for angle in range(0,360,15):
	t.seth(angle)
	sqr(colors[angle%7])

turtle.mainloop()
