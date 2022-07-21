import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab04/ch04_t12_if_having.py")

        expected = """Success #1
Success #2
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
