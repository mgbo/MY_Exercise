
# -*- coding:utf-8 -*-

import turtle           
import time

def veer(n, col, size):
                        # 1 раз ДО повторения
    t.color(col)        # установить цвет

    for i in range(n):  # повторяем n раза рисунок 1 линии
        t.fd(size)        
        t.fd(-size)        
        t.left(30)     


t = turtle.Turtle()
t.shape("turtle")
t.width(3)

veer(12, 'yellow', 100)
time.sleep(3)
t.seth(-15)
veer(12, 'red', 120)

turtle.done()
