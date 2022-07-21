import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab16/ch016_t12_anonymous_func.py")
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], temp_locals['my_list'])
        expect_output = """[0, 3, 6, 9, 12, 15]
"""
        self.assertEqual(expect_output, output)


if __name__ == '__main__':
    unittest.main()
