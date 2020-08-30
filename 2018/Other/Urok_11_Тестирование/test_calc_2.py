
import unittest
import calc

class CalcTest(unittest.TestCase):
	""" Calc tests """
	
	
	@classmethod
	def setUpClass(cls):
		""" Set up for class """
		print ("setUpClass")
		print ("==========")

	@classmethod
	def tearDownClass(cls):
		""" Tear down for class """
		print ("tearDownClass")
		print ("============")

	def setUp(self):
		print ("Set up for [" + self.shortDescription() + "]")

	def test_add(self):
		""" Add operation test """
		print ("id: " + self.id())
		self.assertEqual(calc.add(1, 2), 3)

if __name__ == "__main__":
	unittest.main()