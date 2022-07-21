import unittest
from tests.unit_test_helper import is_answer




class TestOutput(unittest.TestCase):

    def setUp(self):
        if is_answer:
            from lab.lab18.ch018_t15_class_basics_ans import Triangle
        else:
            from lab.lab18.ch018_t15_class_basics import Triangle
        self.triangle = Triangle(30, 60, 90)

    def test(self):
        self.assertEqual(30, self.triangle.angle1)
        self.assertEqual(60, self.triangle.angle2)
        self.assertEqual(90, self.triangle.angle3)


if __name__ == '__main__':
    unittest.main()
