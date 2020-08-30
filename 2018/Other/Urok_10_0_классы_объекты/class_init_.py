
'''
class Enemy:
	def __init__(self, x):
		self.energy = x

	def get_engergy(self):
		print (self.energy)

jason = Enemy(5)
sandy = Enemy(18)

jason.get_engergy()
sandy.get_engergy()
'''

class Parent():
	def print_last_name(self):
		print ("Robets")

class Child(Parent):
	def print_frist_name(self):
		print ("Bucky")
		