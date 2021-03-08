import unittest
import leapyear

class TestCase(unittest.TestCase):
    
    def test_Fizz(self):
        res = leapyear.isleap(2012)
        self.assertEqual(res[0], "2012 is a leap year")
        

if __name__ == '__main__':
    unittest.main()