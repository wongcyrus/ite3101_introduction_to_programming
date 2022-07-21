import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab01/ch01_t14_review.py")
        print(temp_locals)
        self.assertEqual('Python Syntax', temp_locals['skill_completed'])
        self.assertEqual(13, temp_locals['exercises_completed'])
        self.assertEqual(5, temp_locals['points_per_exercise'])
        self.assertEqual(165, temp_locals['point_total'])


if __name__ == '__main__':
    unittest.main()
