
# -*- coding: utf-8 -*-
import turtle           
import time

def veer(n, col, size, d):
                        # 1 раз ДО повторения
    t.color(col)        # установить цвет

    for i in range(n):  # повторяем n раза рисунок 1 линии
        t.fd(size)        
        t.fd(-size)        
        t.left(30)
        size += d       # в цикле изменяем значение переменной size       


t = turtle.Turtle()
t.shape("turtle")
t.width(3)

veer(6, 'yellow', 60, 20)
t.seth(-15)
veer(7, 'red', 50, 20)

turtle.done()
