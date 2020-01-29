import unittest
from HW01_Boyang_Guo import classify_triangle

class TestHW(unittest.TestCase):

    def test_classify_triangle(self):
        self.assertEqual(classify_triangle(3,3,3), 'this is a equilateral triangle')
        self.assertEqual(classify_triangle(3,3,4), 'this is a isosceles triangle')
        self.assertEqual(classify_triangle(3,4,5), 'this is a right triangle')
        self.assertEqual(classify_triangle(3,6,10), 'this is not a triangle')
        self.assertEqual(classify_triangle(3,4,6), 'this is a scalene triangle')

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
