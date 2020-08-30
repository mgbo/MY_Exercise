
class Hero():
	def __init__(self, name, lavel, race):
		self.name = name
		self.lavel = lavel
		self.race = race
		self.health = 100

	def show_Myhero(self):
		print (self.name + "lavel is " + str(self.lavel) + ". My health is " + str(self.health))

	def lavel_up(self):
		self.lavel +=1

	def set_health(self, new_health):
		self.health = new_health

class SuperHero(Hero):
	def __init__(self, name, level, race, magiclevel):
		super().__init__(name, level, race)
		self.magiclevel = magiclevel
		self.magic = 100

	def makemagic(self):
		""" Use magic """
		self.magic -= 10

	def show_Myhero(self):
		print (self.name + "lavel is " + str(self.lavel) + ". My health is " + str(self.health) +
			" magic is " + str(self.magic).title())




















		