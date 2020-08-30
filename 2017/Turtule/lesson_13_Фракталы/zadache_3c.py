
# -*- coding: utf-8 -*-
import turtle           
import time

def koch_line(size, n):
	if n == 0:        # рисуем линию и дальше не идем
		t.fd(size)
		return

	t.right(45)
	a = size/2    # иначе разбиваем отрезок
	koch_line(a, n-1)
	t.left(90)
	koch_line(a, n-1)
	t.right(45)

#----------  конец функции ------------

t = turtle.Turtle()
t.shape("turtle")
t.color('blue')
t.width(3)
t.speed(0)

koch_line(800,6)

turtle.hideturtle()
turtle.done()  
