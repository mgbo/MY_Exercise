
import math

x = float(input())
y = float(input())
x_c = float(input())
y_c = float(input())
r = float(input())


def IsPointInCircle(x, y, x_c, y_c, r):
	dis_p = math.sqrt((x_c - x)*(x_c - x) + (y_c - y)*(y_c - y))

	return dis_p <= r

if IsPointInCircle(x, y, x_c, y_c, r):
	print ("YES")

else:
	print ("NO")