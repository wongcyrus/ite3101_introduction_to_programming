import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab17/ch017_t07_bit_of_this_n_that.py")
        expect_output = """0b100
"""
        self.assertEqual(expect_output, output)


if __name__ == '__main__':
    unittest.main()
