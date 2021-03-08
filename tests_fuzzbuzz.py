import unittest
import fuzzbuzz

class TestCase(unittest.TestCase):
    
    def test_Fizz(self):
        res = fuzzbuzz.fuzzbuzz(5)
        self.assertEqual(res[0], "Buzz")
        

    def test_values(self):
        res = fuzzbuzz.fuzzbuzz(5)
        self.assertEqual(res[1], 1)
        self.assertEqual(res[2], 2)
        self.assertEqual(res[3], 3)
        self.assertEqual(res[4], 4)
if __name__ == '__main__':
    unittest.main()