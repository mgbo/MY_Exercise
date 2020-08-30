

import sys
from operator import itemgetter,attrgetter

class Rub(object):
	""" Класс для работы с рублями и копейками """

	def __init__(self, rub=0, kop=0):
		self.rub = rub
		self.kop = kop
		
	def __str__(self):
		return '{}.{} rub'.format(self.rub, self.kop)

	def __repr__(self):
		return '{}.{} rub'.format(self.rub, self.kop)

	def __lt__(self, other):
		if self.rub == other.rub:
			return self.kop < other.kop

		return self.rub < other.rub

	def __add__(self, other):
		res = Rub()
		total_kop = ((self.rub+other.rub) * 100 + (self.kop + other.kop))

		res.rub = total_kop//100
		res.kop = total_kop%100

		return res

	def __sub__(self, other):
		res = Rub()

		total_self = self.rub * 100 + self.kop
		total_other = other.rub * 100 + other.kop

		if total_self < total_other:
			return 'НЕ хватает денги'

		else:
			total_kop = total_self - total_other
			res.rub = total_kop//100
			res.kop = total_kop%100

			return res

class Goods(object):
	""" Класс описания товара: название и цена"""

	def __init__(self, name='', rub=0, kop=0):
		self.name = name
		self.price = Rub(rub, kop)

	def __str__(self):
		return '{} {}'.format(self.name, self.price)

	def __repr__(self):
		return self.__str__()

def read():
	list_tovar = []
	for d in sys.stdin:
		name, rub, kop = d.split()
		list_tovar.append(Goods(name, int(rub), int(kop)))
	return list_tovar

def test():
	l1 = read()

	t = Goods('total')
	#print (t.price)
	for g in sorted(l1, key= lambda l : l.price, reverse=True):
		print (g)
		t.price +=  g.price	
	print ('-----')
	print (t)



	r,k = map(int, input("Платить за товары : ").split())
	paku = Goods('tender',r,k)


	print (paku.price - t.price)


if __name__ == "__main__":

	test()
	print ("---------------")

	#tovar_1 = Goods('rice',10,50)
	#print (tovar_1)
	'''
	r = Rub(5,10)
	r2 = Rub(5,60)

	l = [r,r2,Rub(5,30)]

	s = Rub()
	for i in l:
		s = s + i
		print (s)

	print (s)

	print ('------------')


	g = Goods('tea',5,6)
	g1 = Goods('rice',5,14)

	ss = Goods('total')

	print (g.price + g1.price)

	sss = [g,g1,Goods('cofe',10,50)]

	for ii in sss:
		ss.price += ii.price
		print (ss.price)
	'''
















