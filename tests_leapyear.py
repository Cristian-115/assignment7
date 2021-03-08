import unittest
import leapyear

class TestCase(unittest.TestCase):
    
    def test_Fizz(self):
        res = leapyear.isleap(2020)
        self.assertEqual(res[0], "2020 not a leap year")
        

if __name__ == '__main__':
    unittest.main()