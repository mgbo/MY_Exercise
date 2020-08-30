
'''
Принадлежит ли точка квадрату - 2
'''

x = float(input())
y = float(input())

def IsPointInSquare(x, y):
	# print ('(-x+1){} >= {}'.format((-x+1), y))
	# print ('(-x+1){} >= y {}'.format((x+1), y))
	# print ('(-x-1){} <= y {}'.format((-x-1), y))
	# print ('(x-1){} <= y {}'.format((x-1), y))

	return (-1<= x <=1 and  y<=-x+1 ) and (-1<= x <=1 and  y<=x+1) and \
	(-1<= x <=1 and y>=-x-1) and (-1<=x <=1 and y>=x-1)

if IsPointInSquare(x, y):
	print ('YES')
else:
	print ("NO")