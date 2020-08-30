
# -*- coding:utf-8 -*-

import turtle

def write(data):
	t.write(data, font= ("Arial",14,"normal"))

t = turtle.Turtle()
t.shape('turtle')
t.turtlesize(10)
ang = t.heading() 
# в переменную ang запомнили угол черепахи
ang = t.heading() + 90    # или изменяем по-другому
                          # или так:
print ang
ang += 90                 # "старое" значение переменной ang увеличили на 90
print ang
ang -= 30                 # "старое" значение переменной ang уменьшили на 30
print ang
ang *= 3                  # "старое" значение переменной ang увеличили в 3 раза
print ang
ang /= 4                  # "старое" значение переменной ang уменьшили в 4 раза
print ang

turtle.done()