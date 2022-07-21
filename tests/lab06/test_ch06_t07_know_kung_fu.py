import unittest

from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        with self.assertRaises(NameError):
            execfile("lab06/ch06_t07_know_kung_fu.py")


if __name__ == '__main__':
    unittest.main()
