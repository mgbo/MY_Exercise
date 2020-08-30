
from zadache_1_class import Time12
import unittest

class TestTime12(unittest.TestCase):

	@classmethod
	def SetUpClass(cls):
		print ("___ SetUpClass___")

	def Setup(self):
		print ("--- Setup ---")
		self.t_12 = Time12(2,5)
		self.t_22 = Time12(5,0)

	def Test_time_add(self):
		self.assertTupleEqual(self.t_12.round(),("5:0"))


if __name__ == "__main__":
	unittest.main()