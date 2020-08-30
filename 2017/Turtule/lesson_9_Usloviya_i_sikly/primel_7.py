
#-*- coding:utf-8-*-
import turtle
import time
import math

def write(data):
	t.write(data,font = ("Arial",14,"normal"))

def new_color(col):
	if col== 'red':
		col='gold'
	else:
		col ='red'
	t.pencolor(col)
	return col #Возвращем (return) новый цвет

t = turtle.Turtle()
t.shape("turtle")
t.width(3)

col = 'yellow'
t.color(col)

for i in range(5):
	write(i)
	t.fd(50)
	col=new_color(col) 
	# функция new_col вернула другой цвет и мы этот цвет записали в col
turtle.done()





