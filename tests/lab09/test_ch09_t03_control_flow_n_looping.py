import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab09/ch09_t03_control_flow_n_looping.py")

        expected = """0
2
4
6
8
10
12
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
