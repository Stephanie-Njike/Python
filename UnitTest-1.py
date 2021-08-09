"""
 Example of unit tests
"""

import unittest

def my_abs(a):
    if a <= 0:
        return -a
    return a

def my_abs2(b):
    if b <= 0:
        return b
    return b

class TestAbs(unittest.TestCase):
    
    def test_my_abs(self):
        """
        Check that my_app function is working correctly 
        """
        self.assertEqual(my_abs(5), 5)
        self.assertEqual(my_abs(0), 0)
        self.assertEqual(my_abs(-5), 5)

        self.assertEqual(my_abs2(5), 5)
        self.assertEqual(my_abs2(0), 0)
        # This assertion will launch an error
        #self.assertEqual(my_abs2(-5), 5)

if __name__ == '__main__':
    unittest.main()
