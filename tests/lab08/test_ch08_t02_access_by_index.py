import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab08/ch08_t02_access_by_index.py")

        expected = """Adding the numbers at indices 0 and 2...
12
Adding the numbers at indices 1 and 3...
14
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
