
# -*- coding: utf-8 -*-

import turtle
from time import sleep

def write(data):
	t.write(data, font=("Arial",14,"normal"))

def midline(x1,x2):

    start = t.position()  # запомним в start место черепахи
    print "start point : ",start
    t.color("darkgreen")
    t.up()
                          # поставим черепаху в нужное место
                          # x1, x2 - тоже переменные
                          # они помнят координаты 
    t.goto(x1, 0)
                          # нарисуем линию между x1 и x2
    t.down()
    t.goto(x2, 0)
    sleep(1)
                          
    mid = (x2 - x1) / 2   # ВЫЧИСЛИМ середину mid (координату x)
                          # нарисуем половину линии (отрезка)
    print "mid : ", mid
    t.pencolor("gold")    # другим цветом
    
    #x1 = (x2+x1)/2        # изменим ЗНАЧЕНИЕ x1 на координату середины
    x1 = x2 - mid         # изменим ЗНАЧЕНИЕ x1 на координату середины
    print "X1 : ", x1
    sleep(3)
    t.goto(x1, 0)         # переместим черепаху и нарисуем линию
    sleep(3)
    write(mid)            # напечатаем ЗНАЧЕНИЕ mid
    t.up()                # вернем черепаху на место start (где была)
    t.goto(start)

t = turtle.Turtle()
t.shape("turtle")
t.width(3)

midline(-200, 300)            

turtle.done()