
class tt():
	def __init__(self, h=0, m=0):
		self.h = h # часы от 0 до 11
		self.m = m # минуты от о до 59

	def t(self,ttt):
		if ttt.m == self.m:
			return 1
		else:
			return 2

if __name__ == "__main__":
	t1 = tt(2,3)
	t2 = tt(2,3)

	t1.t(t2)
	