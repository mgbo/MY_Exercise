class Date():
	month = ['январь', 'февраль']
	def __init__(self, day, month, year):
		self.day = day
		self.month = month
		self.year = year
		self.month_name = Date.month[month-2]

	def __str__(self):
		return ('{}:{}:{}'.format(self.day, self.month, self.year))


d1 = Date(20, 2, 2018)
print (d1)
print (d1.month_name)
