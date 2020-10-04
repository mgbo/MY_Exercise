
class A:
	def __init__(self, arg):
		self.arg = arg

	def __str__(self):
		return str(self.arg)


class B:
	def __init__(self, *args):
		self.aList = []
		for i in args:
			self.aList.append(A(i))

	def __getitem__(self, i):
		return self.aList[i]


group = B(5, 10, 'abc')
print(group.aList[1], type(group.aList[1]))
print (group[0]) # __getitem__ method အသုံးပြုလိုက်တဲ့အတွက်





