import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab16/ch016_t14_try_it.py")
        self.assertListEqual([1, 4, 9, 16, 25, 36, 49, 64, 81, 100], temp_locals['squares'])
        expect_output = """[36, 49, 64]
"""
        self.assertEqual(expect_output, output)


if __name__ == '__main__':
    unittest.main()
