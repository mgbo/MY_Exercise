

import turtle
import sys

fp = sys.stdin # для бесконечный вход

t = turtle.Turtle()
t.color('darkgreen')

colors = [
	"blue",    # colors[0]
	"red",     # colors[1]
	"gold",    # colors[2]
	"green",   # colors[3]
	"violet"   # colors[4]
]

n = len(colors)
i = 0                                 # НОМЕР первого цвета 0

for string in fp:                     # для всех строк
	t.color(colors[i%n])                # берем цвет по его номеру i
	x, y = map(int, string.split())      # прочитали p = (x,y) для 1 точки
	t.setpos((x, y))                      # передвинули черепаху в точку (x, y)
	i +=1
 


turtle.done()


