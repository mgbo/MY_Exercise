
class A:
	def __init__(self, x =[]):
		self.x = x
		self.y = 1

	def foo(self):
		return self.y

	def qqq(self):
		pass

class B(A):
	def __init__(self,x = []):
		super().__init__(x)
		self.x.append('banna')
		self.y = 2

	def foo(self):
		return -(self.y)

	def zzz(self):
		return A.foo(self) #так можно добраться до методов базовых классов

if __name__ == "__main__":
	b = B(['apple'])

	print (b.x) # apple,banna
	print (b.y) # 2

	#print (dir(b))

	print(b.foo())
	print (b.zzz())






