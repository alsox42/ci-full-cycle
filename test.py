import unittest
from main import soma 

class TestSoma(unittest.TestCase):
   def test_soma(self):
       self.assertEqual(soma(10, 20), 30)
       self.assertEqual(soma(-1, 1), 0)
       self.assertEqual(soma(0, 0), 0)

if __name__ == '__main__':
   unittest.main()