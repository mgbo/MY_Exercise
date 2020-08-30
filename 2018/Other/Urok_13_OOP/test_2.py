
class Matrix:
	def __init__(self, m):
		self.m = Matrix.flated(m)
		self.row = len(m)
		self.col =len(m[0])
		self.__ori = m

	def flated(m):
		"form 2D to 1D"
		list_m = []
		for x in m:
			list_m.extend(x)
			#print ("flated : ",list_m)
		return list_m

	def size(self):
		return self.row, self.col

	def __add__(self,other):
		new_add = []
		if self.size() == other.size():
			for i in range(self.row):
				nn= self.m[i] + other.m[i]
				new_add.append(nn)

			new_m = Matrix([new_add])
			print (new_m)

			new_m.size()
			return new_m

	def __repr__(self):
		return "Rank :({},{})---> Matrix : {} ".format(self.row,self.col,self.m)
	
	def display(self):
		s=''
		for i in range(self.col):
			s +=(str(self.m[i]))
		s ='\t'.join(s)

		#s = '\n'.join(s)
		return s

	def __str__(self):
		s = '\n'.join([' '.join([str(item) for item in row]) for row in self.__ori])
		return s+'\n'


M_1 = Matrix([[1,2,3],[4,5,6]])
#print (M_1.size())
print (M_1)
print (M_1.display())

M_2 = Matrix([[1,2,3],[4,5,6]])
#print(M_2.size())
print(M_2)

print (str(M_1) == str(M_2))
print(M_1+M_2)

#print (M_1+M_2)



