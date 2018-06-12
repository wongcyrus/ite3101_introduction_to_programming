import unittest
from test.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content = execfile("lab01/ch01_t14_review.py")
        print(temp_locals)
        self.assertEqual(temp_locals['skill_completed'], 'Python Syntax')
        self.assertEqual(temp_locals['exercises_completed'], 13)
        self.assertEqual(temp_locals['points_per_exercise'], 5)
        self.assertEqual(temp_locals['point_total'], 165)


if __name__ == '__main__':
    unittest.main()
