import unittest
from unittest.mock import patch

from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test_word_input(self):
        user_input = ["Cyrus"]
        with patch('builtins.input', side_effect=user_input):
            temp_globals, temp_locals, content, output = execfile("lab05/ch05_t04_check_yourself_more.py")

        self.assertEqual("Welcome to the Pig Latin Translator!\nCyrus\n", output)

    def test_invalid_word_input(self):
        user_input = ["Cyrus!"]
        with patch('builtins.input', side_effect=user_input):
            temp_globals, temp_locals, content, output = execfile("lab05/ch05_t04_check_yourself_more.py")

        self.assertEqual("Welcome to the Pig Latin Translator!\nempty\n", output)

    def test_empty_input(self):
        user_input = [""]
        with patch('builtins.input', side_effect=user_input):
            temp_globals, temp_locals, content, output = execfile("lab05/ch05_t04_check_yourself_more.py")

        self.assertEqual("Welcome to the Pig Latin Translator!\nempty\n", output)


if __name__ == '__main__':
    unittest.main()
