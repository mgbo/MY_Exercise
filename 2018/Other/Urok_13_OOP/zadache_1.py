
class Matrix:
	def __init__(self,m):
		self.m = Matrix.flated(m)
		self.row = len(m)
		self.col = len(m[0])
		self.__oriM = m

	@staticmethod
	def flated(m):
		list_m = []
		for l in m:
			list_m.extend(l)
		return list_m

	def size(self):
		return self.row,self.col

	def reshape(self, r, c):
		self.row = r
		self.col = c

	def __add__(self, m1):
		#if self.kolichestbvo() != m1.kolichestbvo():
		#	raise ValueError,"Нужно Вводить одиноковое Количество строка и столбеца"

		new = []
		for i in range(len(self.m)):
			a = self.m[i] + m1.m[i]
			new.append(a)
		#print (new)
		
		new_m = Matrix([new])
		#print (new_m)

		new_m.reshape(self.row, self.col)
		return new_m

	def __mul__(self,koeifi):
		new = []
		for i in range(len(self.m)):
			a = self.m[i] * koeifi
			new.append(a)

		new_m = Matrix([new])

		new_m.reshape(self.row, self.col)
		return new_m

	def transpose(self):
		pass

	def __repr__(self):
		return ("Matrix row={} col={} {}".format(self.row, self.col, self.m))
	
	
	def __str__(self):
		s = '\n'.join(['\t'.join([str(item) for item in row]) for row in self.__oriM])
		return s

	'''
	def __str__(self):
		s = '\n'.join(['\t'.join([str(item) for item in row]) for row in m])
		return s
	'''


m_1 = Matrix([[1, 1, 2], [0, 100, 10]])
print (m_1)
print (str(m_1)=='1\t1\t1\n0\t100\t10')

m_2 = Matrix([[1, 1, 1], [0, 100, 10]])
print(str(m_2))

print(str(m_1) == str(m_2))

print(repr(m_1+m_2))

m_3 = Matrix([[1, 1, 0], [0, 2, 10], [10, 15, 30]])
print (str(m_3))
print (repr(m_3*15))












