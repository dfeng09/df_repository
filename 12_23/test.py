import unittest
from interface_test import Rectangle

class TestRectangle(unittest.TestCase):
    def test_area(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_perimeter(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.perimeter(), 30)

if __name__ == '__main__':
    unittest.main()

