import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab17/ch017_t05_int_func_2nd_param.py")
        expect_output = """1
2
7
4
5
201
"""
        self.assertEqual(expect_output, output)


if __name__ == '__main__':
    unittest.main()
