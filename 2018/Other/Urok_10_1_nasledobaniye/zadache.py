
class Crow:
	def __init__(self, basket, apple=0):
		self.basket = basket # корзина из которой ворона ворует яблоки
		self.apple = apple # сколько яблоке в 1 час сможет своровать ворона

	def steal (self):
		self.basket -= self.apple

		return self.basket

class Worker:
	def __init__(self, basket, apple=0):
		self.basket = basket # корзина в воторую работник кладет яблоки
		self.apple = apple # сколько яблок в 1 час собирает работник

	def work(self):
		self.basket += self.apple
		return self.basket

if __name__ == "__main__":

	work_1 = Worker(15,5)
	print (work_1.work())

	crow_1 = Crow(15,5)
	print (crow_1.steal())



