
"""
Если нужно, допишите функции в класс Segment1. 
Даны отрезки - по 1 на строку, целые числа через пробел. 
Выровнять отрезки по левому краю (по самому левому) и напечатать в том же порядке.
Input:
0 9
-1 3
-10 -7
5 11
Output:
-10 -1
-10 -6
-10 -7
-10 -4
"""

class Segment1(object):
	"""Класс Segment1 описывает отрезки на оси Х"""

	def __init__(self, start=0, finish=0):
		# Эта функция вызывается, когда мы создаем новый объект класса.
		# self - это название переменной, которая указвает на сам объект.
		self.start = start
		self.finish = finish
		self.normalize()

	def __str__(self):
		return ("({},{})".format(self.start,self.finish))

	def __repr__(self):
		return ('({},{}) = {} '.format(self.start, self.finish, self.length()))
	
	def length(self):
		return (self.finish - self.start)

	def normalize(self):
		if self.start > self.finish:
			self.start, self.finish = self.finish, self.start
		
	def flip(self):
		self.start, self.finish = -(self.finish),-(self.start)
		return self.start, self.finish

	def move_add(self, dx=0):
		self.start +=dx
		self.finish +=dx

	def move_diff(self, dx=0):
		self.start -=dx
		self.finish -=dx


#-------------------------------------------
if __name__ == "__main__":
	#n = int(input())

	list_segment = []
	for i in range(4):
		x,y = map(int, input().split())
		list_segment.append(Segment1(x,y))

	'''
	left_x = []
	print ("--------------")
	for n in list_segment:
		print (n.start)
		left_x.append(n.start)

	print (left_x)
	min_left = min(left_x)
	print (min_left)
	'''

	min_left1 = min((s.start for s in list_segment)) # s - это класс (Segment1)
	#print(min_left1)

	for s in list_segment:
		dx = s.start - min_left1
		s.move_diff(dx)
		print(repr(s))

	max_segment = max([s for s in list_segment], key=Segment1.length)
	#print ("Максимальный сегмент",repr(max_segment))

	print("Длина самого большого отрезка : ",max_segment.length())
	print("Самый длинный отрезок : ",max_segment)

	












