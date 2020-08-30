
"""
The syntax of getattr() method is:
	getattr(object, name[, default])
"""

"""
class Person:
	age = 23
	name = 'Adam'
	

p = Person()
print ('The age is :', getattr(p, "age"))
"""

#---------------------------------------
#----------------------------------------

class Container(object):
	def __init__(self):
		self.cards = ['Здравствуйте']
	
	def __getattr__(self, name):
		return self.cards.__getattribute__(name)
	
	def __repr__(self):
		#s =''.join([str(s) for s in self.cards])
		#return s
		return '\t'.join(self.cards)

c = Container()
c.cards.append('hello')
c.cards.append('hi')
print (repr(c.cards))

