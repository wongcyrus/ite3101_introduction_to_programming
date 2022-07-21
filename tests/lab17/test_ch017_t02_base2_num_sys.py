import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab17/ch017_t02_base2_num_sys.py")
        expect_output = """1 2 3 4 5 6 7 ******
4
9
"""
        self.assertEqual(expect_output, output)


if __name__ == '__main__':
    unittest.main()
