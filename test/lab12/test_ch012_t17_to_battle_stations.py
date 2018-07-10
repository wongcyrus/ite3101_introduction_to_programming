import sys
import unittest
from unittest.mock import patch

from unit_test_helper import is_answer
from unit_test_helper.console_test_helper import get_function_output, mock_randint


class TestOutput(unittest.TestCase):

    def load(self):
        self.myModule = __import__('lab12.ch012_t17_to_battle_stations' + "_ans" if is_answer else "", globals(),
                                   locals(),
                                   [''], 0)

    def tearDown(self):
        del sys.modules[self.myModule.__name__]
        return

    @patch("builtins.input", side_effect=["1", "1", "1", "1", "1", "1", "1", "1"])
    @patch("random.randint", mock_randint)
    def test_guess_correct(self, mock_input):
        output, value = get_function_output(lambda: self.load())
        expect = """Turn 1
Congratulations! You sank my battleship!
"""
        self.assertEqual(expect, output)

    @patch("builtins.input", side_effect=["1", "2", "1", "2", "1", "2", "1", "2"])
    @patch("random.randint", mock_randint)
    def test_guess_incorrect(self, mock_input):
        output, value = get_function_output(lambda: self.load())
        expect = """Turn 1
You missed my battleship!
O O O O O
O O X O O
O O O O O
O O O O O
O O O O O
Turn 2
You guessed that one already.
O O O O O
O O X O O
O O O O O
O O O O O
O O O O O
Turn 3
You guessed that one already.
O O O O O
O O X O O
O O O O O
O O O O O
O O O O O
Turn 4
You guessed that one already.
Game Over
"""
        self.assertEqual(expect, output)

    @patch("builtins.input", side_effect=["1", "10", "1", "10", "1", "10", "1", "10", "1", "10"])
    @patch("random.randint", mock_randint)
    def test_invalid(self, mock_input):
        output, value = get_function_output(lambda: self.load())
        expect = """Turn 1
Oops, that's not even in the ocean.
O O O O O
O O O O O
O O O O O
O O O O O
O O O O O
Turn 2
Oops, that's not even in the ocean.
O O O O O
O O O O O
O O O O O
O O O O O
O O O O O
Turn 3
Oops, that's not even in the ocean.
O O O O O
O O O O O
O O O O O
O O O O O
O O O O O
Turn 4
Oops, that's not even in the ocean.
Game Over
"""
        self.assertEqual(expect, output)


if __name__ == '__main__':
    unittest.main()
