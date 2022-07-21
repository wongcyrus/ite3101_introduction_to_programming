import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab17/ch017_t10_not_that_hard.py")
        expect_output = """-2
-3
-4
-43
-124
"""
        self.assertEqual(expect_output, output)


if __name__ == '__main__':
    unittest.main()
