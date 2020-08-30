
class Matrix:
	def __init__(self, m):
		self.m = m
		self.row = len(m)
		self.col = len(m[0])

	def display(self):
		pass

	def __str__(self):
		pass

def intput(r, c):
	s = [[input() for i in range(c)]for j in range(r)]

m_1 = Matrix([[1,2,3],[4,5,6]])
#print(m_1.display())
#print (m_1)