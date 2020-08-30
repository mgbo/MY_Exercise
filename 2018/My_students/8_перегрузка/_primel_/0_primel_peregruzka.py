
class Point(object):

	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def __str__(self):
		return '({},{})'.format(self.x, self.y)

	def __repr__(self):
		return self.__str__()
		#return '({} {})'.format(self.y, self.y)


	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

	def __lt__(self, other):
		 """ Меньше та точка, у которой меньше х. При одинаковых x, та, у которой меньше y."""
		 if self.x == other.x:
		 	return self.y<other.y
		 	'''
		 	if self.y < other.y:
		 		return True

		 	else:
		 		return False
		 	'''

		 return self.x<other.x


def test():
	p0 = Point(3, 5)
	p1 = Point(3, 5)
	p2 = Point(-1, 7)
	p3 = Point(3, 1.17)

	'''
	print (p0==p1) # Treue

	print ('p2 < p0', p2 <p0) # True
	assert (p2 < p0)

	print ('p0 < p2', p0 <p2) # False
	assert (p2 < p0)
	'''

	a = [p0,p1,p2,p3]
	print (a)
	pmin = min(a)
	print ('pmin : ',pmin)

	b = sorted(a)
	print (b)

if __name__ == "__main__":
	test()


