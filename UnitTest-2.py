import unittest

def mediane(a,b,c):
    if a <= b and b <= c:
       return b
    if a <= c and c <= b:
       return c
    if b <= a and a <= c:
       return a
    if b <= c and c <= a:
       return c
    if c <= b and b <= a:
       return b
    if c <= a and a <= b:
       return a
    

class TestAbs(unittest.TestCase):
    
    def test_mediane(self):
        """
        Check that mediane function is working correctly 
        """
        self.assertEqual(mediane(2,2,2), 2)
        self.assertEqual(mediane(1,2,3), 2)
        self.assertEqual(mediane(6,4,5), 5)
        self.assertEqual(mediane(8,-3,11), 8)


if __name__ == '__main__':
    unittest.main()
