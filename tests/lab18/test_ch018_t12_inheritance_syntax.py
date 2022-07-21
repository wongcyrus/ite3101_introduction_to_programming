import unittest
from tests.unit_test_helper import is_answer




class TestOutput(unittest.TestCase):

    def setUp(self):
        if is_answer:
            from lab.lab18.ch018_t12_inheritance_syntax_ans import Triangle
        else:
            from lab.lab18.ch018_t12_inheritance_syntax import Triangle
        self.triangle = Triangle(1, 2, 3)

    def test(self):
        if is_answer:
            from lab.lab18.ch018_t12_inheritance_syntax_ans import Shape, Triangle
        else:
            from lab.lab18.ch018_t12_inheritance_syntax import Shape, Triangle
        self.assertIsInstance(self.triangle, Shape)
        self.assertIsInstance(self.triangle, Triangle)
        self.assertEqual(1, self.triangle.side1)
        self.assertEqual(2, self.triangle.side2)
        self.assertEqual(3, self.triangle.side3)


if __name__ == '__main__':
    unittest.main()
