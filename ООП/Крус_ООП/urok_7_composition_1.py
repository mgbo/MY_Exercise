
class WinDoor:
	def __init__(self, w, h):
		self.square = w * h


class Room:
	def __init__(self, l, w, h):
		self.length = l
		self.width = w
		self.height = h
		self.wd = []

	def fullSurface(self):
		return 2 * self.height * (self.length + self.width)

	def addWD(self, w, h):
		self.wd.append(WinDoor(w, h))

	def workSurface(self):
		new_square = self.fullSurface()
		for i in self.wd:
			new_square -= i.square

		return new_square

	def wallpapers(self, l, w):
		return int(self.workSurface()/(w*l)) + 1






