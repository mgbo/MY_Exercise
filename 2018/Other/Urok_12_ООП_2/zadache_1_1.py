
class Rub:
	def __init__(self, r=0, kop=0):
		self.r = r
		self.kop = kop

	def getRub(self):
		self.r = int(input())
		self.kop = int(input())

	def __str__(self):
		return "%d руб : %d коп"%(self.r,self.kop)

class Dol:
	def __init__(self, d=0, cen=0):
		self.d = d
		self.cen = cen

	def getRub(self):
		self.d = int(input())
		self.cen = int(input())

	def __str__(self):
		return "%d dollar : %d cen"%(self.d,self.cen)

	def rub_t_dol(rr=None): # rr - это класс Rub
		dd = Dol()
		t_cen = ((rr.r*100 + rr.kop)/6533)*100

		dd.d = t_cen//100
		dd.cen = t_cen%100

		return dd

class Shop():

	def __init__(self, d1=0, cen1=0):
		self.d1 = d1
		self.cen1 = cen1

	def price(self):
		print ("Морожное стоит :")
		self.d1 = int(input("dollar : "))
		self.cen1 = int(input("Cents : "))

	def __str__(self):
		return "%d dol , %d cen"%(self.d1,self.cen1)

	@classmethod
	def sdache_cls(cls, pric, dol_0):
		total_cen = pric.d1*100 + pric.cen1 # prize of icecreen to cen
		dol_new = Dol.rub_t_dol(dol_0) # rubles change to dollar

		total_cen_1 = dol_new.d * 100 + dol_new.cen


		if total_cen_1>=total_cen:
			sub = total_cen_1 - total_cen

			return 'Ваша сдача : {}'.format(cls(sub//100,sub%100))
		else:
			return ("не хватает денги")


if __name__ == "__main__":

	d1 = Dol(50,4)
	print (d1.d)

	r1 = Rub(130,66)
	print (r1)

	
	d2 = Dol.rub_t_dol(r1) # dollat to rubles
	print ("{} >>>>>>>>>>> {}".format(r1,d2))
	

	p1 = Shop()
	p1.price()
	print(p1)

	ans = Shop.sdache_cls(p1,r1)
	print (ans)
	






