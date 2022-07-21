import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab16/ch016_t09_reversing_list.py")
        self.assertListEqual([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], temp_locals['backwards'])


if __name__ == '__main__':
    unittest.main()
