import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab16/ch016_t10_stride_length.py")
        self.assertListEqual([100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0], temp_locals['backwards_by_tens'])
        expect_output = """[100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
"""
        self.assertEqual(expect_output, output)


if __name__ == '__main__':
    unittest.main()
