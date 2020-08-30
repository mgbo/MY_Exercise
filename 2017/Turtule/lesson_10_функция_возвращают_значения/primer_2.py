
# -*- coding: utf-8 -*-
import turtle           
import time

def write(data):
    t.write(data, font=("Arial", 14, "normal"))

def sq0(size, col):
  p0 = t.pos()      #  запомним от какой точки будем рисовать
  
                    # найдем центр квадрата
  t.up()
  t.fd(size/2)
  t.left(90)
  t.fd(size/2)
  centr = t.pos()   # запомним центр квадрата в переменную centr
  time.sleep(1)     # ждем 1 секунду
  
  t.goto(p0)        # вернемся в начальную точку       
  t.left(-90)       # восстановим направление
  t.color(col)
  t.down()
                    # нарисуем квадрат
  for i in range(4):
    t.fd(size)
    t.left(90)
  t.up()
                  
  return centr      # ВЕРНЕМ ЗНАЧЕНИЕ centr


t = turtle.Turtle()
t.shape("turtle")
t.width(3)
pc = sq0(100, "blue")   # Нарисуем квадрат и получим точку центра pc
                        # вычислять ее больше не нужно
                        # pc вычисляет функция sq0()

t.color('red')          # после функции черепаха стала красной
time.sleep(1)           # ждем 1 секунду
t.goto(pc)              # поставим черепаху на этот центр

write(pc)               # напишем координаты точки pc

turtle.done()