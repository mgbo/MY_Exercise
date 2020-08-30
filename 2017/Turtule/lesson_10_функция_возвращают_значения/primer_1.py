# -*- coding: utf-8 -*-
import turtle           
import time

def write(data):
    t.write(data, font=("Arial", 14, "normal"))

def carre(size, col):
  p0 = t.pos()      #  запомним от какой точки будем рисовать
  t.color(col)
  t.down()
                    # вычислим координаты середины
  xc = size/2
  write(xc)
  yc = size/2
  write(yc)
                   # нарисуем квадрат
  for i in range(4):
    t.fd(size)
    t.left(90)
  t.up()
  time.sleep(3)
                
  t.goto(xc, yc)    # встанем на центр

  
  centr = t.pos()   # запомним точку центра
  
  #t.goto(p0)        # вернемся в начальную точку
  
  return centr      # ВЕРНЕМ ЗНАЧЕНИЕ центр


t = turtle.Turtle()
t.shape("turtle")
t.width(3)
pc = carre(100, "blue") # Нарисуем квадрат и получим точку центра pc
                        # вычислять ее больше не нужно
                        # pc вычисляет функция carre()

#t.goto(pc)              # поставим черепаху на этот центр
#write(pc)

turtle.done()

