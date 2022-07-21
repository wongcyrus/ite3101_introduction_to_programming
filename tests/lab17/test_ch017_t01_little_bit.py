import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab17/ch017_t01_little_bit.py")
        expect_output = """0
10
0
13
38
-89
"""
        self.assertEqual(expect_output, output)


if __name__ == '__main__':
    unittest.main()
