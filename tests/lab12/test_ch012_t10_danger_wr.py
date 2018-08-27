import sys
import unittest
from unittest.mock import patch

from ..console_test_helper import get_function_output, is_answer


class TestOutput(unittest.TestCase):

    def load(self):
        self.myModule = __import__('lab12.ch012_t10_danger_wr' + "_ans" if is_answer else "", globals(), locals(), [''],
                                   0)

    def tearDown(self):
        del sys.modules[self.myModule.__name__]
        return

    @patch("builtins.input", side_effect=["1", "1"])
    @patch("random.randint", lambda x, y: 1)
    def test_guess_correct(self, mock_input):
        output, value = get_function_output(lambda: self.load())
        self.assertTrue("Congratulations! You sank my battleship!" in output)

    @patch("builtins.input", side_effect=["1", "2"])
    @patch("random.randint", lambda x, y: 1)
    def test_guess_incorrect(self, mock_input):
        output, value = get_function_output(lambda: self.load())
        expect = """1
1
You missed my battleship!
O O O O O
O O X O O
O O O O O
O O O O O
O O O O O
"""
        self.assertEqual(expect, output)


if __name__ == '__main__':
    unittest.main()
