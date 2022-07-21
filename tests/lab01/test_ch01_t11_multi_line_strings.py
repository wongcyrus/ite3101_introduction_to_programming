import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab01/ch01_t11_multi_line_strings.py")
        print(temp_locals)
        self.assertEqual('The old pond,\nA frog jumps in:\nPlop!\n', temp_locals['haiku'])


if __name__ == '__main__':
    unittest.main()
