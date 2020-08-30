
# -*- coding: utf-8 -*-
import turtle           
import time

def koch_line(size, n):
  if n == 0:        # рисуем линию и дальше не идем
    t.fd(size)
    return
  a = size/3        # иначе разбиваем отрезок 
                    # и вместо него делаем набор отрезков  
  koch_line(a, n-1)
  t.left(60)
  koch_line(a, n-1)
  t.right(120)
  koch_line(a, n-1)
  t.left(60)
  koch_line(a, n-1)
                    # конец функции

def koch_tri(size,n):
	for i in range(3):
		p0 = t.pos()
		koch_line(size, n)
		t.right(120)

t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(0)


t.color('blue')

#koch_line(200,1)
koch_tri(200,0)
turtle.done()  
