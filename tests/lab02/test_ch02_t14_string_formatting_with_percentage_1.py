import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        result = get_script_output("lab02/ch02_t14_string_formatting_with_percentage_1.py")
        self.assertEqual("Let's not go to Camelot. 'Tis a silly place.\n", result)


if __name__ == '__main__':
    unittest.main()
