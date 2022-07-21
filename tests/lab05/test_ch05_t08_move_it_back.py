import unittest
from unittest.mock import patch

from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test_word_input(self):
        user_input = ["Cyrus"]
        with patch('builtins.input', side_effect=user_input):
            temp_globals, temp_locals, content, output = execfile("lab05/ch05_t08_move_it_back.py")
        print(temp_locals)
        self.assertEqual("cyrus", temp_locals["word"])
        self.assertEqual("c", temp_locals["first"])
        self.assertEqual("cyruscay", temp_locals["new_word"])

    def test_invalid_word_input(self):
        user_input = ["Cyrus!"]
        with patch('builtins.input', side_effect=user_input):
            temp_globals, temp_locals, content, output = execfile("lab05/ch05_t08_move_it_back.py")

        self.assertEqual("empty\n", output)

    def test_empty_input(self):
        user_input = [""]
        with patch('builtins.input', side_effect=user_input):
            temp_globals, temp_locals, content, output = execfile("lab05/ch05_t08_move_it_back.py")

        self.assertEqual("empty\n", output)


if __name__ == '__main__':
    unittest.main()
