

import math

x = float(input())
y = float(input())


def IsPointInCircle(x, y):
	radius = 2

	dis_p = math.sqrt((-1 - x)*(-1 - x) + (1 - y)*(1 - y))
	# print ("Length from center of circle --> {}".format(dis_p))
	# print ("2x+2 : {}  >=  y {}".format((2*x+2), y))
	# print ("-x : {} >= y {}".format((-x), y))

	return (y>=2*x + 2 and y >= -x and dis_p<= radius) \
			or (y<=2*x + 2 and y <= -x and dis_p>= radius)

if IsPointInCircle(x, y):
	print ("YES")

else:
	print ("NO")