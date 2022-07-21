import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab08/ch08_t09_more_for.py")

        expected = """[1, 4, 9, 16, 25]
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
