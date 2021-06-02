import unittest
from fields import rectangle, triangle


class FieldsTestCase(unittest.TestCase):
    def setUp(self):
        self.a = 2
        self.b = 10

    def test_rectangle_with_correct_values(self):
        result = rectangle(self.a, self.b)
        self.assertEqual(result, 20)

    def test_triangle_with_correct_values(self):
        result = triangle(self.a, self.b)
        self.assertEqual(result, 10)


if __name__ == '__main__':
    unittest.main()
