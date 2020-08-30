
# -*- coding: utf-8 -*-
import turtle           
import time


def tree(size, d, ang, n):
	if n == 0:
		t.color('darkgreen')# дерево закончило расти, возвращаемся
		return

		#t.color='brown'
	t.fd(size)                  # рисуем ветку
	t.left(ang)                 # поворачиваемся рисовать левую веточку
	tree(size-d, d, ang, n-1)   # рисуем левое поддерево (веточку и дальше)

	#time.sleep(5)
	#t.color('brown')
	t.left(-2*ang)              # поворачиваемся рисовать правую веточку
	tree(size-d, d, ang,  n-1)  # рисуем правое поддерево (веточку и дальше)
	#t.color('brown')
	t.left(ang)                 # возвращаем направление ветки
	t.fd(-size)
	t.color('brown')                 # возвращаемся в начало ветки

#--------  конец функции --------

t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(1)

t.seth(90)
t.up()
t.bk(200)
t.down()
t.color('brown')
tree(100, 20, 30, 2)

turtle.done() 
