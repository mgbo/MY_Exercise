
# -*- coding: utf-8 -*-

import turtle
from time import sleep

# напишем функцию write, которая пишет нужными буквами
def write(data):
	t.write(data, font=("Arial",14,"normal"))

def line3(size):
	t.color("blue")
	xy = t.pos() #запомним где черепаха, короткое мия t.pos()
	# xy - это переменная, которая запомнила где черепаха
	print (xy)
	
	sleep(2)
	t.fd(size)
	sleep(2)
	t.fd(size)
	t.up()
	t.goto(xy)
	write(xy)
	sleep(2)

t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.goto(-200,0)
sleep(5)
line3(100)
turtle.done()



