import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        result = get_script_output("lab01/ch01_t04_handling_errors.py")
        print(result)
        self.assertEqual("How do you make a hot dog stand?\nYou take away its chair!\n", result)


if __name__ == '__main__':
    unittest.main()
