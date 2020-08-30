
from math import pi

class Circle:
	def __init__(self, x=0, y=0, r=0):
		self.x = x
		self.y = y
		self.r = r

	def __str__(self):
		return "({},{},{})".format(self.x,self.y,self.r)

	def read(self):
		self.x,self.y,self.r = map(int,input().split())

	def area(self):
		a = pi*self.r * self.r
		return a
	def perimetr(self):
		return 2*pi*self.r

	def zoom(self, k):
		self.r *=k

	def is_crossed(self, c): # пересекается или нет окружность с окружностью с?
		d2 = (self.x - c.x)**2 + (self.y - c.y)**2
		r2 =(self.r + c.r)**2
		return d2 <=r2

c1 = Circle()
c2 = Circle()
'''
c1.r = 3
c2.r = 5
c2.x = 1
c2.y = 1
'''
c1.read()
c2.read()

print (c1)
print (c2)

'''
ans = c1.area()
print (ans)
'''



















