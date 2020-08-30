class Backet():
	def __init__(self):
		self.apple = 0

	def __str__(self):
		return 'В корзине %d яблок' %(self.apple)

	def add(self, apple):
		self.apple += apple
		return self.apple

	def sub(self, apple):
		self.apple -= apple
		if self.apple < 0:
			self.apple = 0
		return self.apple
		
class Person:
	def __init__(self, basket, apple=0, name=''):
		#print ("Появился кто то")
		self.basket = basket # корзина, куда кладут или откуда берут
		self.apple = 0 # переменная, где будет храниться сколько яблок в час может собрать или урать эта персона
		self.set_apple(apple)# сделаем присовоение с проверкой
		self.name = name

	def set_apple(self, apple):
		if apple<0:
			set.apple = 0
		else:
			self.apple = apple%100
		print (self)

	def __str__(self):
		s = 'Кто-то будет %d яблок в час'% (self.apple)
		s = s + '\n' + "в корзине " + str(self.basket)
		return s

class Worker(Person):
	def __init__(self, basket, apple=0, name=''):
		super().__init__(basket, apple, name) # вызываем конструктор базового класса
		print ('Я работник %s, я собираю %s в корзине.'%(self.name,self.apple))
	

	def work(self):
		self.basket.add(self.apple)
		print ("работник положил %d яблок"%(self.apple))
		print (self.basket)
		return self.basket

class Crow(Person):
	def __init__(self, basket, apple=0, name ="Kpaa"):
		super().__init__(basket, apple)
		print ('я вороны воруют %s яблок'%(self.apple))

	def Steal(self):
		self.basket.sub(self.apple)
		print (self.basket)
		return self.basket


if __name__ == "__main__":

	b = Backet()
	w1 = Worker(b,10,"Ivan")
	w1.work()
	
	print ('\n')

	cor1 = Crow(b,7)
	cor1.Steal()

		












