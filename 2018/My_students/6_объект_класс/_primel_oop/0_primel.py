
class A:
	pass

a = A()

print (type(a)) # <class '__main__.A'>
print (type(A)) # <class 'type'>
print (type(1))

print (isinstance(1,int))
print (isinstance(a,A))

print ('--------------')

class A:
	def f(self):
		print ('Hello')

print (type(A.f))# <class 'function'>

a = A()
print (type(a.f))# <class 'method'>