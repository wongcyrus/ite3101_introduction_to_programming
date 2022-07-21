import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab16/ch016_t11_practice_makes_perfect.py")
        self.assertListEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
                             temp_locals['to_21'])
        self.assertListEqual([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21], temp_locals['odds'])
        self.assertListEqual([8, 9, 10, 11, 12, 13, 14], temp_locals['middle_third'])


if __name__ == '__main__':
    unittest.main()
