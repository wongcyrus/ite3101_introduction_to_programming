import unittest
from ..console_test_helper import is_answer

if is_answer:
    from lab.lab18.ch018_t18_inheritance_ans import Triangle, Equilateral
else:
    from lab.lab18.ch018_t18_inheritance import Triangle, Equilateral


class TestOutput(unittest.TestCase):

    def setUp(self):
        self.equilateral = Equilateral()

    def test(self):
        self.assertIsInstance(self.equilateral, Triangle)
        self.assertIsInstance(self.equilateral, Equilateral)
        self.assertTrue(self.equilateral.check_angles())
        self.assertEqual(3, self.equilateral.number_of_sides)
        self.assertEqual(60, self.equilateral.angle1)
        self.assertEqual(60, self.equilateral.angle2)
        self.assertEqual(60, self.equilateral.angle3)


if __name__ == '__main__':
    unittest.main()
