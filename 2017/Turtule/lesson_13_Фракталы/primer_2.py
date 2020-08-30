
# -*- coding: utf-8 -*-
import turtle           
import time

tones = [
  'yellow',   # tones[0]
  'gold',     # tones[1]
  'orange',   # tones[2]
  'red',      # tones[3]
  'violet',   # tones[4]
  'blue',     # tones[5]
  'green'     # tones[6]
  ]

def koch_line(size, n):
	if n == 0:        # рисуем линию и дальше не идем
		t.fd(size)
		return
	a = size/3        # иначе разбиваем отрезок 
                    # и вместо него делаем набор отрезков  
	koch_line(a, n-1)
	t.left(60)
	
	koch_line(a, n-1)
	t.right(120)
	koch_line(a, n-1)
	t.left(60)
	koch_line(a, n-1)
	#конец функции

t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(0)

for i in range(5):    # i = 0..4
  p0 = t.pos()           # запомнили начальную позицию в p0
  t.color(tones[i])      # новой итерации - новый цвет
  koch_line(300, i)      # нарисовали кривую Коха глубины i
  
  t.up()                 # вернулись на начальную позицию
  t.goto(p0)
  t.down()
  time.sleep(1)          # ждем 1 секунду

turtle.done()  
