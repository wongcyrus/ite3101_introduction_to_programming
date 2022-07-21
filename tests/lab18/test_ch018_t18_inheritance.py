import unittest
from tests.unit_test_helper import is_answer




class TestOutput(unittest.TestCase):

    def setUp(self):
        if is_answer:
            from lab.lab18.ch018_t18_inheritance_ans import Triangle, Equilateral
        else:
            from lab.lab18.ch018_t18_inheritance import Triangle, Equilateral
        self.equilateral = Equilateral()

    def test(self):
        if is_answer:
            from lab.lab18.ch018_t18_inheritance_ans import Triangle, Equilateral
        else:
            from lab.lab18.ch018_t18_inheritance import Triangle, Equilateral
        self.assertIsInstance(self.equilateral, Triangle)
        self.assertIsInstance(self.equilateral, Equilateral)
        self.assertTrue(self.equilateral.check_angles())
        self.assertEqual(3, self.equilateral.number_of_sides)
        self.assertEqual(60, self.equilateral.angle1)
        self.assertEqual(60, self.equilateral.angle2)
        self.assertEqual(60, self.equilateral.angle3)


if __name__ == '__main__':
    unittest.main()
