import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab17/ch017_t04_bin_func.py")
        expect_output = """0b1
0b10
0b11
0b100
0b101
"""
        self.assertEqual(expect_output, output)


if __name__ == '__main__':
    unittest.main()
