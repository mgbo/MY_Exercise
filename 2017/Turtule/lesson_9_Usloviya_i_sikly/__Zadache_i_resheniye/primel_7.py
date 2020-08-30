
# -*- coding: utf-8 -*-
import turtle           
import time

def write(data):
    t.write(data, font=("Arial", 14, "normal"))

def new_color(col):
    if col == 'red':      # если цвет был красный
        col = 'gold'      # станет желтый
    else :                # иначе (если был желтый)
        col = 'red'       # станет красный
    t.pencolor(col)
    return col            # ВОЗВРАЩАЕМ (return) новый цвет

t = turtle.Turtle()
t.shape("turtle")
t.width(3)

col = 'yellow'            # первый отрезок желтый
t.color(col)
for i in range(5):
    write(i)
    t.fd(50)
    col = new_color(col) # функция new_col ВЕРНУЛА другой цвет и мы этот цвет записали в col

turtle.done()

