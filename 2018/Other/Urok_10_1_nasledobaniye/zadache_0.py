
class Backet:
	def __init__(self):
		self.apple = 0

	def add(self,apple):
		self.apple += apple
		return self.apple

	def sub(self, apple):
		self.apple -=apple
		if self.apple < 0:
			self.apple = 0
		return self.apple

	def __str__(self):
		return "Сумма яблок в корзине %d"%(self.apple)


class Person:
	def __init__(self, backet, apple=0, name=''):
		self.backet = backet
		self.apple = 0
		self.name = name
		self.set_apple(apple)

	def set_apple(self, apple):
		if apple<0:
			self.apple = 0
		else:
			self.apple = apple%100
		print ("Self : ",self)

	def __str__(self):
		s = 'кто то, будет %d яблок в час'%(self.apple)
		s = s + '\n' + 'в корзине '+ str(self.backet)
		return s


class Worker(Person):
	def __init__(self, backet, apple=0, name=''):
		super().__init__(backet, apple, name)
		print ('я работник %s, я собираю %s яблок'%(str(self.name),str(self.apple)))

	def work(self):
		self.backet.add(self.apple)
		print (self.backet)
		return self.backet

if __name__ == "__main__":

	b = Backet()
	w1 = Worker(b,150,"Ivan")
	w1.work()

	print('\n')

	w2 = Worker(b,20,'ko ko')
	w2.work()



















