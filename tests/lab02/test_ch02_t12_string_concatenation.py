import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        result = get_script_output("lab02/ch02_t12_string_concatenation.py")
        self.assertEqual("Spam and eggs\n", result)


if __name__ == '__main__':
    unittest.main()
