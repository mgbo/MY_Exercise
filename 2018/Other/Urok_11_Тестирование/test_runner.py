
import unittest
import test_calc

calcTestSuite = unittest.TestSuite()

calcTestSuite.addTest(unittest.makeSuite(test_calc.CalcTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcTestSuite)