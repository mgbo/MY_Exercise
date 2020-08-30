
import math
import sys

class Point:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def __str__(self):
		return '({},{})'.format(self.x, self.y)

	def dist_x(self, other):
		"""Квадрат расстояния до точки other"""
		dx = self.x - other.x
		
		return abs(dx)

	def dist_y(self, other):
		dy = self.y - other.y
		return abs(dy)

	def dir(self, other):
		""" длина диагоналей """
		dx = self.dist_x(other)
		dy = self.dist_y(other)

		return dx*dx + dy*dy

	def dist0(self):
		return dist2(Point(0,0))

	def movePoint(self, other=None):
		if other is None:
			return
		self.x +=other.x
		self.y +=other.y

	def isSame(self, other):
		if self.x == other.x and self.y == other.y:
			return 1
		else:
			return 0

class Rectangle:
	def __init__(self, lt, rb):
		self.lt = lt
		self.rb = rb
		self.normalize()

	def __str__(self):
		return 'Point of Rectangle is : {},{}'.format(self.lt, self.rb)

	def __repr__(self):
		return '[{},{}] -> length : {}'.format(self.lt,self.rb,self.square())

	def area(self):
		height = self.lt.dist_y(self.rb)
		length = self.lt.dist_x(self.rb)

		return height*length

	def diagonal(self):
		return math.sqrt(self.lt.dir(self.rb))

	def normalize(self):
		if self.lt.x > self.rb.x and self.lt.y < self.rb.y:
			self.lt.x, self.rb.x, self.lt.y, self.rb.y = self.rb.x, self.lt.x, self.rb.y, self.lt.y
		#else:
		#	print ("Правильный Прямоугольник")

	def add_x(self,dx):
		self.rb.x +=dx

	def add_y(self,dy):
		self.rb.y +=dy

	def same_square(self,other):
		if self.square() == other.square():
			print("SAME")
		else:
			print ("NOT SAME")

	def is_cross(self, other):
		if self.lt.y  < other.rb.y or self.rb.y > other.lt.y or self.rb.x > other.lt.x or self.rb.x > other.lt.x:
			return False
		else:
			return True

	def lt_0(self):
		x1 = self.lt.dist_x(self.lt)
		y1 = self.lt.dist_y(self.lt)

		x2 = self.rb.dist_x(self.lt)
		y2 = self.rb.dist_y(self.lt)

		return Rectangle(Point(x1,y1),Point(x2,-y2))

	def lb_0(self):
		x1 = self.lt.dist_x(self.lt)
		y1 = self.lt.dist_y(self.rb)

		x2 = self.rb.dist_x(self.lt)
		y2 = self.rb.dist_y(self.rb)

		return Rectangle(Point(x1,y1),Point(x2,y2))

	def alignment(self):
		pass 


if __name__ == '__main__':
	
	def read_rect(str):
		x1, y1, x2, y2 = map(int, str.split())
		s = Rectangle(Point(x1,y1),Point(x2,y2))
		return s

	lis_rect = []

	for str in sys.stdin:
		ss = read_rect(str)
		lis_rect.append(ss)

	print ('---------')

	# Площади Прямоугольников
	print ("Площади Прямоугольников : ")
	for r in lis_rect:
		print (r,r.area())

	print ('------------')

	#  Передвинуть их так, чтобы левая верхняя точка каждого прямоугольника лежала в (0, 0).
	print('левая верхняя точка (0,0) :')
	for r_cen in lis_rect: 
		print(r_cen.lt_0())

	print ('------------')

	# Передвинуть их так, чтобы левая нижняя точка каждого прямоугольника лежала в (0, 0).
	print('левая нижняя точка (0,0) : ')
	for r_cen in lis_rect: 
		print(r_cen.lb_0())

	print ('-----------------')

	'''
	r1 = Rectangle(Point(1,1),Point(3,-2))
	print(r1)
	print(r1.diagonal()/2)
	'''

	r1 = lis_rect[0]
	for lignm in lis_rect[1:]:
		dx = r1.lt.dist_x(lignm.lt)
		dy = r1.lt.dist_y(lignm.lt)

		lignm.add_x(dx)
		lignm.add_y(dy)

		print (lignm)






















