
# -*- coding: utf-8 -*-

import turtle           
import time

def steps(size, n):
                        # 1 раз ДО повторения
    p0 = t.pos()        # запомнили старт в переменную p0 
    t.seth(90)          # повернулись, чтобы начать рисовать много ступенек

    for i in range(n):  # повторяем n раза рисунок 1 ступеньки
        t.fd(size)        
        t.right(90)     
        t.fd(size)        
        t.left(90)     

                        # 1 раз ПОСЛЕ повторения
    t.up()              # вернулись на место старта p0
    t.goto(p0)                              

t = turtle.Turtle()
t.shape("turtle")
t.width(3)

steps(50, 3)

turtle.done()