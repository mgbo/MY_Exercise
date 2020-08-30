
# -*- coding: utf-8 -*-
import turtle           
import time

def write(data):
    t.write(data, font=("Arial", 14, "normal"))


t = turtle.Turtle()
t.shape("turtle")
t.width(3)

col=['red','blue','green','magenta','wheat']
for i in range(5):
	for j in range(4):
		t.color(col[i%5])
		t.fd(100)
		t.lt(90)
	t.up()
	t.rt(90)
	t.fd(100)
	t.lt(90)
	t.down()


turtle.done()
