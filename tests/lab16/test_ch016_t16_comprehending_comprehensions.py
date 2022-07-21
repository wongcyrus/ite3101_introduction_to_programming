import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab16/ch016_t16_comprehending_comprehensions.py")
        self.assertListEqual([3, 5, 6, 9, 10, 12, 15], temp_locals['threes_and_fives'])


if __name__ == '__main__':
    unittest.main()
