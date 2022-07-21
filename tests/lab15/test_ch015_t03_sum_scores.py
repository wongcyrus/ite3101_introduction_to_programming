import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab15/ch015_t03_sum_scores.py")
        expect = """1045.5
"""
        self.assertEqual(expect, output)


if __name__ == '__main__':
    unittest.main()
