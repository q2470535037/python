import unittest

class TestCalculator(unittest.TestCase):
    def test_logo(self):
        self.assertEqual(2 + 2, 4)
    def test_addition(self):
        self.assertEqual(5-3,2)
if __name__=='__main__':
    unittest.main()

