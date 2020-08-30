
from my_first import my_contains, first_ele
import unittest

class TestMyFun(unittest.TestCase):
	def my_con(self):
		self.assertTrue(my_contains(3,[1,2,3]))

	def my_f(self):
		self.arrertTrue(first_ele([1,2,3],1))

if __name__ == "__main__":
	unittest.main(exit=False)


