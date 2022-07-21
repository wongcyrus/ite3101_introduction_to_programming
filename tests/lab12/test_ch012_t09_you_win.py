import unittest

from unittest.mock import patch

from tests.unit_test_helper import is_answer
from tests.unit_test_helper.console_test_helper import get_function_output


def load():
    if is_answer:
        from lab.lab12.ch012_t09_you_win_ans import ship_row, ship_col, guess_row, guess_col
    else:
        from lab.lab12.ch012_t09_you_win import ship_row, ship_col, guess_row, guess_col
    return ship_row, ship_col, guess_row, guess_col


class TestOutput(unittest.TestCase):

    @patch("builtins.input", side_effect=["1", "1"])
    @patch("random.randint", lambda x, y: 1)
    def test_guess_correct(self, mock_input):
        output, value = get_function_output(load)
        self.assertTrue("Congratulations! You sank my battleship!" in output)

    @patch("builtins.input", side_effect=["1", "2"])
    @patch("random.randint", lambda x, y: 1)
    def test_guess_incorrect(self, mock_input):
        output, value = get_function_output(load)
        self.assertFalse("Congratulations! You sank my battleship!" in output)


if __name__ == '__main__':
    unittest.main()
