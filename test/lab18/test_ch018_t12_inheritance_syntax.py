import unittest
from unit_test_helper import is_answer

if is_answer:
    from lab18.ch018_t12_inheritance_syntax_ans import Shape, Triangle
else:
    from lab18.ch018_t12_inheritance_syntax import Shape, Triangle


class TestOutput(unittest.TestCase):

    def setUp(self):
        self.triangle = Triangle(1, 2, 3)

    def test(self):
        self.assertIsInstance(self.triangle, Shape)
        self.assertIsInstance(self.triangle, Triangle)
        self.assertEqual(1, self.triangle.side1)
        self.assertEqual(2, self.triangle.side2)
        self.assertEqual(3, self.triangle.side3)


if __name__ == '__main__':
    unittest.main()
