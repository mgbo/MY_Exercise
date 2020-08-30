

import unittest
import calc_1
 
class CalcTest(unittest.TestCase):

	def test_add(self):
		self.assertEqual(calc_1.add(1, 2), 3)

	def test_sub(self):
		self.assertEqual(calc_1.sub(5, 2), 3)

	def test_mul(self):
		self.assertEqual(calc_1.mul(10, 2), 20)

	def test_div(self):
		self.assertEqual(calc_1.div(15, 3), 5)

class CalcExTests(unittest.TestCase):

	def test_sqrt(self):
		self.assertEqual(calc_1.sqrt(4), 2)

	def test_pow(self):
		self.assertEqual(calc_1.pow(2, 2), 4)

		
if __name__ == '__main__':
	unittest.main()



