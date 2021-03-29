#https://www.youtube.com/watch?v=6tNS--WetLI
#https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        result = calc.add(10,5)
        self.assertEqual(result,15)
        # same as... 
        self.assertEqual(calc.add(10,5),15)
        # possible edge cases..
        self.assertEqual(calc.add(-1,1),0)
        self.assertEqual(calc.add(-1,-1),-2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10,5),5)
        self.assertEqual(calc.subtract(-1,1),-2)
        self.assertEqual(calc.subtract(-1,-1),0)
    
    def test_multiply(self):
        self.assertEqual(calc.multiply(10,5),50)
        self.assertEqual(calc.multiply(-1,1),-1)
        self.assertEqual(calc.multiply(-1,-1),1)

    def test_divide(self):
        self.assertEqual(calc.divide(10,5),2)
        self.assertEqual(calc.divide(-1,1),-1)
        self.assertEqual(calc.divide(-1,-1),1)

#To test: 
    # python -m unittest test_calc.py 
# or...
if __name__ == '__main__':
    unittest.main()
