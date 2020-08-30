
from math import sqrt

class Point:
	""" класс работы с точками на плоскости XY"""
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def read(self):
		self.x, self.y = map(int, input().split())
		#self.x = int(input())
		#self.y = int(input())


	def shift(self, dx=0, dy=0):
		self.x += dx
		self.y += dy

	def Dis_Two_P(self, a):
		dx = self.x - a.x
		dy = self.y - a.y

		d = sqrt((dx*dx) + (dy*dy))

		return d

	def dx(self, a):
		return self.x - a.x

	def dy (self, a):
		return self.y - a.y

	def __str__(self):
		return "(%d,%d)"%(self.x, self.y)


if __name__ == "__main__":
	P1 = Point()
	print(P1) # (0,0)

	P1.read()
	print(P1)

	P2 = Point()
	P2.read()
	
	print(P1)
	print (P2)

	P2.shift(5,0)
	print(P2)

	dx_1 = P1.dx(P2)
	print (dx_1)

	#dis_p = P1.Dis_Two_P(P2)
	#print("На сколько нудно пердвинуть точу от P1 до P2 : ",dis_p)

	

























