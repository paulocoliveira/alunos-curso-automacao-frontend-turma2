import unittest

class TestCalculator(unittest.TestCase):
    
    def setUpClass():
        print("Start")
    
    def test_sum(self):
        self.assertEqual(1+1, 2)
    
    def test_sub(self):
        self.assertEqual(2-1, 1)

    def tearDownClass():
        print("End")