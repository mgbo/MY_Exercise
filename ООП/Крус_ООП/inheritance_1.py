
class Table:
	def __init__(self, l, w, h):
		self.length = l
		self.width = w
		self.height = h


class KitchenTable(Table):
	# def setPlace(self, p):
	# 	self.place = p

	def __init__(self, l, w, h, p):
		# Table.__init__(self, l, w, h);
		super().__init__(l, w, h)
		self.place = p

class DeskTable(Table):
	def square(self):
		return self.width * self.length