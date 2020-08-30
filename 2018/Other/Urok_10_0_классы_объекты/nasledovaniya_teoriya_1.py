
import math

class Point():
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def dist0(self):
		""" расстояние до точки (0,0) """
		return math.hypot(self.x, self.y)

class Circle(Point): # класс Circle расширяет функциональность класса Point
	def __init__(self, x=0, y=0, r=0):
		super().__init__(x,y) # вызов конструктора родительского класса
		#self.x = x
		#self.y = y
		self.r = r

	def area(self):
		return math.pi * self.r**2

	def edge_dist(self):
		return abs(self.dist0() - self.r) # доступен метод базового класса self.dist0()

p = Point(3,4)
c = Circle(4, 3, 2.5)

print (p.dist0())
print (c.dist0())

print (c.area())


















		