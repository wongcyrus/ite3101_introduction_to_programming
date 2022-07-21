import unittest

from unittest.mock import patch

from tests.unit_test_helper import is_answer


class TestOutput(unittest.TestCase):

    @patch("builtins.input", side_effect=["1", "2"])
    def test(self, mock_input):
        if is_answer:
            from lab.lab12.ch012_t07_and_seek_ans import guess_row, guess_col
        else:
            from lab.lab12.ch012_t07_and_seek import guess_row, guess_col
        self.assertEqual(1, guess_row)
        self.assertEqual(2, guess_col)


if __name__ == '__main__':
    unittest.main()
