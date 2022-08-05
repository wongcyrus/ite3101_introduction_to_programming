import unittest
from unittest.mock import patch

from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        user_input = ["Cyrus", "Happy", "38"]
        with patch('builtins.input', side_effect=user_input):
            result = get_script_output("lab02/ch02_t15_string_formatting_with_percentage_2.py")
        self.assertEqual("Ah, so your name is Cyrus, your quest is Happy, and your favorite color is 38.\n", result)


if __name__ == '__main__':
    unittest.main()
