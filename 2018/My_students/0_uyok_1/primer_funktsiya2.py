
#-*- coding:utf-8 -*-
from math import sqrt

def length(x1,y1,x2,y2):
	dx = x1 - x2
	dy = y1 - y2
	res = sqrt(dx*dx + dy*dy )
	return res

x1, y1, x2, y2 = map(int,input().split()) 
# прочитали сразу много чисел из 1 строки

dist = length(x1,y1,x2,y2)

print (dist)


