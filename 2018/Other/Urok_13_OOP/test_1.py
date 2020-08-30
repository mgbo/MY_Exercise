
class Matrix:
	def __init__(self, m):
		self.li = Matrix.flated(m)
		self.row = len(m)
		self.col = len(m[0])

	@staticmethod
	def flated(m):
		#"from 2D list make 1D list, return 1D list"
		lst = []

		for row in m:
			lst.extend(row)
		'''
		# drugoy sposob
		for row in m:
			for x in row:
				lst.append(x)
		'''
		return lst 

	def kolichestbvo(self):
		'''
		r = self.row
		c = self.col
		koli = r,c

		return koli
		'''
		#return ("Количество строка и столбеца ({},{}) ".format(self.row, self.col))

		return (self.row, self.col)

	def add(self, m1):
		#if self.kolichestbvo() != m1.kolichestbvo():
		#	raise ValueError,"Нужно Вводить одиноковое Количество строка и столбеца"
		
		new = []
		for i in range(len(self.li)):
			a = self.li[i] + m1.li[i]
			new.append(a)
		#print (new)
		
		new_m = Matrix([new])
		print (new_m)

		new_m.reshape(self.row, self.col)
		return new_m


	def reshape(self, r, c):
		self.row = r
		self.col = c
		
	def __add__(self, other):
		add_matrix = self.li + other.li
		return (add_matrix)

	def __repr__(self):
		return ("Matrix row={} col={} {}".format(self.row, self.col, self.li))
	
	def __str__(self):
		new =[]
		c_1 = self.li[:3]
		c_2 = self.li[3:]
		new.append(c_1)
		new.append(c_2)

		s = '\n'.join([' '.join([str(item) for item in row]) for row in new])
		return s+'\n'
	
	
m = Matrix([[1,0,9],[1,2,3],[4,5,6]])
#ma = m.flated([[1,0,-5],[1,0,10]])
#print (type(ma),ma) # [[1, 0, -5], [1, 0, 10]]
print ("Matrix 1 : ")
print(m)
print (m.kolichestbvo())


m1 = Matrix([[11,0,3],[12,0,3],[15,2,3]])
print("Matrix 2 : ",m1)

#print (m+m1)

#m.add(m1)
#print (m.add(m1))
