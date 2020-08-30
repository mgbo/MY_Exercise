
import turtle
import sys
import math

t = turtle.Turtle()
ip = sys.stdin

ind = int(input("Номер индекс : "))
print (ind)

lis_p = []
def list_p():
	for i in ip:
		x, y = map(int, i.split())
		lis_p.append((x,y))
	return lis_p


def min_p(ind):
	l_p = list_p()
	x_0, y_0 = l_p[ind]
	print ("IDEX --> (x, y) -->({}, {})".format(x_0, y_0))

	x_1, y_1 = l_p[0]
	d_0 = t.distance((x_0, y_0), (x_1, y_1))
	print ("FIRST : {} : ({}, {})".format(d_0, x_1, y_1))

	for i in l_p[1:]:
		x, y = i
		if x != x_0 and y!= y_0:
			d = math.sqrt((x-x_0)*(x-x_0) + (y - y_0)*(y - y_0))
			print ("distance :{} and ({},{}),({}, {})".format(d, x_0, y_0, x, y))

		if d_0 > d:
			x_1, y_1 = x, y

	return x_1, y_1

m_x , m_y = min_p(ind)
print ("MIN", m_x, m_y)

def dot_p(t, ind):
	l = list_p()
	print (l)
	
	for i in range(len(l)):
		x, y = l[i][0], l[i][1]

		if x == m_x and y == m_y:
			t.color('red')
			t.pu()
			t.setpos((x,y))
			t.pd()
			t.dot(10)

		elif i == ind:
			t.color('green')
			t.pu()
			t.setpos((x,y))
			t.pd()
			t.dot(10)

		else:
			t.color('blue')
			t.pu()
			t.setpos((x,y))
			t.pd()
			t.dot(10)


		


dot_p(t, ind)

			
turtle.done()




