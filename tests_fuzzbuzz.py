import unittest
import fuzzbuzz

class TestCase(unittest.TestCase):
    
    def test_Fizz(self):
        res = fuzzbuzz.fuzzbuzz(5)
        self.assertEqual(res[0], "Buzz")
        



if __name__ == '__main__':
     unittest.main()