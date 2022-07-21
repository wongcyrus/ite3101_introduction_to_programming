import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab04/ch04_t14_elif.py")

        expected = """-1
0
1
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
