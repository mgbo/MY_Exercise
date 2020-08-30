

'''
Задача 3a. Далекая точка
Даны точки.
Нарисовать точку (0, 0) черным.
Нарисовать точки синим. Самую далекую от (0,0) точку красным.

using points.txt
'''

import turtle
import sys

# turtle.dot(size=None, *color) # нарисовать точку радиусом 

# wn = turtle.Screen()
# wn.bgcolor('black')

t = turtle.Turtle()
t.width(5)

fb = ('Arial', 14, 'normal')
ip = sys.stdin

maxp_0 = 0

t.dot(10) # нарисовать точку

# добавить все элементы(dis, x1, x2) в списку d
d = []
for string in ip:
	x1, x2 = map(int,string.split())
	dis = t.distance(x1,x2)
	d.append([dis, x1, x2])

# d.sort(key=lambda l: l[0])
# print (d)

m_d = max(d, key= lambda l: l[0])
m_d = m_d[0] # Наибольшое растояние от точки (0,0)

for i in d:
	d_m, x, y = i
	
	if d_m != m_d:
		t.color('blue')
	else:
		t.color('red')

	t.pu()
	t.setpos((x,y))
	t.pd()
	t.dot(10)

# print (t.distance(100, 0)) # 100 растояние от точки(0,0) до (100, 0)
turtle.done()


