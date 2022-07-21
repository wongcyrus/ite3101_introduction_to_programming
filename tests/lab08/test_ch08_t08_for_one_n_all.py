import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab08/ch08_t08_for_one_n_all.py")

        expected = """2
18
6
16
10
14
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
