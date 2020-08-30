
import unittest

class TestStringMethods(unittest.TestCase):

	def test_1(self):
		self.assertEqual('foo'.upper(),'FOO')

	def test_2(self):
		self.assertTrue('FOO'.isupper())
		self.assertFalse('foo'.isupper())

	def test_3(self):
		s = "Hello World"
		self.assertTrue(s.split(),['Hello','World'])

if __name__ == "__main__":
	unittest.main()