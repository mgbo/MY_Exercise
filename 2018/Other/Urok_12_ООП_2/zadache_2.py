
class Rub:
	def __init__(self, r=0, kop=0):
		self.r = r
		self.kop = kop

	def getRub(self):
		self.r = int(input())
		self.kop = int(input())

	def __str__(self):
		return "%d рульей : %d копей"%(self.r,self.kop)

	def dol_to_rub(dd):
		ch_rub = Rub()

		t_kop = (dd.d1*100  + dd.cen1) * 65.33

		ch_rub.r = t_kop//100
		ch_rub.kop = t_kop%100

		return ch_rub

class Dol:
	def __init__(self, d=0, cen=0):
		self.d = d
		self.cen = cen

	def getDol(self):
		self.d = int(input())
		self.cen = int(input())

	def __str__(self):
		return "%d dollar : %d cen"%(self.d,self.cen)

	def rub_t_dol(rr): # rr - это класс Rub
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
		return "The Price is : %d dollar , %d cen"%(self.d1,self.cen1)

	@classmethod
	def sdache_cls(cls, pric, dol_0):
		total_cen = pric.d1*100 + pric.cen1 # prize of icecreen to cen
		dol_new = Dol.rub_t_dol(dol_0) # rubles change to dollar

		total_cen_1 = dol_new.d * 100 + dol_new.cen

		if total_cen_1>=total_cen:
			sub = total_cen_1 - total_cen
			dol_sda = cls(sub//100,sub%100)
			print ("\nВаша сдача : ")
			print (dol_sda)
			#return dol_sda
			#return cls(sub//100,sub%100)
			Rub_sda = Rub.dol_to_rub(dol_sda)
			print (Rub_sda)
			
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



