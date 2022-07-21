import unittest
from unittest.mock import patch

from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        user_input = ["Cyrus"]
        with patch('builtins.input', side_effect=user_input):
            temp_globals, temp_locals, content, output = execfile("lab05/ch05_t02_input.py")

        self.assertEqual(temp_locals["original"], "Cyrus")


if __name__ == '__main__':
    unittest.main()
