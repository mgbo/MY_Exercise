
from math import sqrt

def length(x1,y1,x2,y2):
	dx = x1-x2
	dy = y1 - y2
	res = sqrt(dx*dx + dy*dy)
	return res

x1,y1,x2,y2 = map(float,input().split())

ans = length(x1,y1,x2,y2)

print (ans)
