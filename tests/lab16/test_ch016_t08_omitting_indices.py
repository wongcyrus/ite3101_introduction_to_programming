import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab16/ch016_t08_omitting_indices.py")
        self.assertListEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], temp_locals['my_list'])
        expect_output = """[1, 3, 5, 7, 9]
"""
        self.assertEqual(expect_output, output)


if __name__ == '__main__':
    unittest.main()
