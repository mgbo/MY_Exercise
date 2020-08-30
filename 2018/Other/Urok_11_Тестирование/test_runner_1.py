
import unittest
import tests_calc1


calcTestSuite = unittest.TestSuite()

calcTestSuite.addTest(unittest.makeSuite(tests_calc1.CalcTest))
calcTestSuite.addTest(unittest.makeSuite(tests_calc1.CalcExTests))


print ("count of tests: " + str(calcTestSuite.countTestCases()) + '\n' )


runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcTestSuite)
