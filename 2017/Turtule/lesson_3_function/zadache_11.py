
# -*- coding: utf-8 -*-

import turtle         
from time import sleep 

# Это прямоугольник (rectangle).
# Одна сторона у него в 3 раза больше другой.
# Линии красные.
# 2 параметра: первый col (цвет внутри) , второй size (размер)
def rect (col, size):
    t.color("red", col)   # "red" - цвет линии, col - цвет внутри
    t.begin_fill()
    t.forward(size)
    t.left(90)
    t.forward(size/3)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size/3)
    t.left(90)
    t.end_fill()
    
t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(0)

rect("yellow", 300)
t.left(90)
rect("violet", 120)

t.hideturtle()
turtle.done()
