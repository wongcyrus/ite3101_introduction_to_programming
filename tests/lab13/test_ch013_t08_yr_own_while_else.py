import sys
import unittest
from unittest.mock import patch

from ..console_test_helper import get_function_output, is_answer
from ..timeout import timeout


class TestOutput(unittest.TestCase):

    def load(self):
        self.myModule = __import__('lab13.ch013_t08_yr_own_while_else' + "_ans" if is_answer else "", globals(),
                                   locals(),
                                   [''], 0)

    def tearDown(self):
        del sys.modules[self.myModule.__name__]
        return

    @timeout(1)
    @patch("builtins.input", side_effect=["1"])
    @patch("random.randint", lambda x, y: 1)
    def test_win(self, mock_input):
        output, value = get_function_output(lambda: self.load())
        expect = "You win!\n"
        self.assertEqual(expect, output)

    @timeout(1)
    @patch("builtins.input", side_effect=["2", "2", "1"])
    @patch("random.randint", lambda x, y: 1)
    def test_win2(self, mock_input):
        output, value = get_function_output(lambda: self.load())
        expect = "You win!\n"
        self.assertEqual(expect, output)

    @timeout(1)
    @patch("builtins.input", side_effect=["2", "2", "2"])
    @patch("random.randint", lambda x, y: 1)
    def test_lost(self, mock_input):
        output, value = get_function_output(lambda: self.load())
        expect = "You lose.\n"
        self.assertEqual(expect, output)


if __name__ == '__main__':
    unittest.main()
