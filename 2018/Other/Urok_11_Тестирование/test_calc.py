

import unittest
import calc
 
class CalcTest(unittest.TestCase):

	def test_add(self):
		self.assertEqual(calc.add(1, 2), 3)

	def test_sub(self):
		self.assertEqual(calc.sub(5, 2), 3)

	def test_mul(self):
		self.assertEqual(calc.mul(10, 2), 20)

	def test_div(self):
		self.assertEqual(calc.div(15, 3), 5)
		
		
if __name__ == '__main__':
	unittest.main()



