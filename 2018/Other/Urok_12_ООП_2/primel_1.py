
class A:
	x = 3
	def __init__(self,x):
		self.x = x

	def zzz(self):
		#print (x)
		print (A.x)
		print (self.x)

	def __add__(self, a):
		return self.x + a.x 

if __name__ == "__main__":
	a = A(7)
	a.zzz()

	a1 = A(10)
	a1.zzz()

	a1.x = 100
	A.x = 22
	a1.zzz()

	ans = a1 + a
	print (ans)








