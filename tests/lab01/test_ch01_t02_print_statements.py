import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        result = get_script_output("lab01/ch01_t02_print_statements.py")
        print(result)
        self.assertTrue("Hello" in result)


if __name__ == '__main__':
    unittest.main()
