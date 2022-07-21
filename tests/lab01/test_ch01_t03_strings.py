import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        result = get_script_output("lab01/ch01_t03_strings.py")
        print(result)
        self.assertTrue("Hello" in result)
        self.assertGreater(len(result), len("Hello "))


if __name__ == '__main__':
    unittest.main()
