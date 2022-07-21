import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        result = get_script_output("lab02/ch02_t07_upper.py")
        self.assertEqual("NORWEGIAN BLUE\n", result)


if __name__ == '__main__':
    unittest.main()
