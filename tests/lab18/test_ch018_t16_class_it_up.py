import unittest
from tests.unit_test_helper import is_answer




class TestOutput(unittest.TestCase):

    def setUp(self):
        if is_answer:
            from lab.lab18.ch018_t16_class_it_up_ans import Triangle
        else:
            from lab.lab18.ch018_t16_class_it_up import Triangle
        self.triangle = Triangle(30, 60, 90)
        self.triangle_invalid = Triangle(10, 60, 90)

    def test(self):
        self.assertTrue(self.triangle.check_angles())
        self.assertFalse(self.triangle_invalid.check_angles())


if __name__ == '__main__':
    unittest.main()
