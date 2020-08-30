
from math import sqrt

def length(x1,y1,x2,y2):
	dx = x1-x2
	dy = y1 - y2
	res = sqrt(dx*dx + dy*dy)
	return res

def sq(x1,y1,x2,y2,x3,y3):
	a = length(x1,y1,x2,y2)
	b = length(x2,y2,x3,y3)
	c = length(x3,y3,x1,y1)
	
	p = (a+b+c)/2
	
	res = sqrt(p*(p-a)*(p-b)*(p-c))
	
	return res
	
x1,y1,x2,y2,x3,y3 = map(float,input().split())

sq_tri = sq(x1,y1,x2,y2,x3,y3)

print (sq_tri)


