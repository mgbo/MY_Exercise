

import math
import sys

class Point:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def __str__(self):
		return '({},{})'.format(self.x, self.y)


	def diff(self, other=object):
		if other is None:
			other = Point(0,0)

		dx = self.x - other.x
		dy = self.y - other.y

		return Point(dx,dy)

	def dist0(self):
		return dist2(Point(0,0))

	def movePoint(self, other=None):
		if other is None:
			return
		self.x +=other.x
		self.y +=other.y

	def gotoPoint(self, d=None):
		if d is None:
			return Point(self.x, self.y)

		p = Point(self.x + d.x, self.y + d.y)
		#print ('::::',p)
		return p

	def dist_x(self, other):
		"""Квадрат расстояния до точки other"""
		dx = self.x - other.x
		
		return dx

	def dist_y(self, other):
		dy = self.y - other.y
		return dy


class Rectangle:
	def __init__(self, lt, rb):
		self.lt = lt or Point()
		self.rb = rb or Point()
		self.normalize()

	def __str__(self):
		return 'Point of Rectangle is : {}, {}'.format(self.lt, self.rb)

	def __repr__(self):
		return '[{},{}] -> length : {}'.format(self.lt,self.rb,self.square())

	def area(self):
		height = self.lt.dist_y(self.rb)
		length = self.lt.dist_x(self.rb)

		return height*length

	def normalize(self):
		if self.lt.x > self.rb.x and self.lt.y < self.rb.y:
			self.lt.x, self.rb.x, self.lt.y, self.rb.y = self.rb.x, self.lt.x, self.rb.y, self.lt.y

	def lt_0(self):
		zero = Point(0,0)
		d_zero = zero.diff(self.lt)
		#print (d_zero)

		lt = self.lt.gotoPoint(d_zero)
		rb = self.rb.gotoPoint(d_zero)

		return Rectangle(lt, rb)

	def lb_0(self):
		x1 = self.lt.dist_x(self.lt)
		y1 = self.lt.dist_y(self.rb)

		x2 = self.rb.dist_x(self.lt)
		y2 = self.rb.dist_y(self.rb)

		p1 = Point(x1,y1)
		p2 = Point(x2,y2)

		return Rectangle(p1,p2)
	
	def alignment(lis_rect):
		ll = []
		r = lis_rect[0]
		ll.append(r)
		#print ('r :', r)
		for rr in lis_rect[1:]:
			#print ('rr',rr)
			xx = r.lt.dist_x(rr.lt)
			yy = r.lt.dist_y(rr.lt)

			p = Point(xx,yy)
			#print ("---",p)

			lt = rr.lt.gotoPoint(p)
			rb = rr.rb.gotoPoint(p)

			#print ("lllll",lt)
			ll.append(Rectangle(lt,rb))

		return ll
	
	def center(self):
		c_x = (self.lt.x + self.rb.x)/2
		c_y = (self.lt.y - self.rb.y)/2

		p1_x = self.lt.x - (c_x)
				
		return Rectangle(Point(p1_x,c_y),Point(-p1_x,-c_y))


if __name__ == '__main__':
	
	print()
	def read_rect(str):
		x1, y1, x2, y2 = map(int, str.split())
		s = Rectangle(Point(x1,y1),Point(x2,y2))
		return s

	lis_rect = []

	for str in sys.stdin:
		ss = read_rect(str)
		lis_rect.append(ss)

	print ('-----------------')

	# Площади Прямоугольников
	print ("Площади Прямоугольников : ")
	for r in lis_rect:
		print (r,r.area())

	print ('-----------------')
	print ('Левая верхняя точка : ')
	for r in lis_rect:
		new = r.lt_0()
		print (new)


	print ('-----------------')
	print ('Левая нижняя точка (0,0) :')
	for r in lis_rect:
		rect_lb = r.lb_0()
		print (rect_lb)

	
	print ('-----------------')
	print ('Выравниевание всех Прямоуголльниов по первому Прямоугольнике ')
	new_ag = Rectangle.alignment(lis_rect)
	for n in new_ag:
		print (n)


	print ('-----------------')
	print("Центр (пересечение диагоналей) :")
	for r in lis_rect:
		c_ret = r.center()
		print(c_ret)


	print ('\n----------------\n')
	print ('Original Point : ')
	for i in lis_rect:
		print (i)
	










