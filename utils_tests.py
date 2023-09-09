import unittest
from utils import * 

class TestUtils(unittest.TestCase):
    def testReversed(self):
        self.assertEqual(reversed(1234), 4321)
        with self.assertRaises(TypeError):
            reversed('1234')
        with self.assertRaises(TypeError):
            reversed(1.123)
    
    def testFormatter(self):
        self.assertEqual(formatter(1234), ('0b10011010010', '0o2322'))
        with self.assertRaises(TypeError):
            formatter("1234")
        with self.assertRaises(TypeError):
            formatter(1.234)

if __name__ == '__main__':
    unittest.main()