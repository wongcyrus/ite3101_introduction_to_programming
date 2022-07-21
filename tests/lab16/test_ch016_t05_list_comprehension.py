import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab16/ch016_t05_list_comprehension.py")
        self.assertListEqual([4, 16, 36, 64, 100], temp_locals['even_squares'])
        expect_output = """[4, 16, 36, 64, 100]
"""
        self.assertEqual(expect_output, output)


if __name__ == '__main__':
    unittest.main()
