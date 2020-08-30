
class Matrix(object):
	def __init__(self, n, m, init=True):
		self.n = n
		self.m = m
		if init:
			self.rows = [[0]*n for i in range(m)]
		else:
			self.rows = []

def main():
	m1 = Matrix(3,3)
	print (m1.rows) #[[0, 0, 0], [0, 0, 0], [0, 0, 0]]

	m2 = Matrix(3,-1)
	print (m2.rows) # []

if __name__ == "__main__":
	main()