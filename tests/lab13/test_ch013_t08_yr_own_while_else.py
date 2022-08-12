import importlib
import sys
import unittest
from unittest.mock import patch

from tests.unit_test_helper import is_answer
from tests.unit_test_helper.console_test_helper import get_function_output
from tests.unit_test_helper.timeout import timeout


class TestOutput(unittest.TestCase):
    def load(self):
        self.my_module = importlib.import_module(
            'lab.lab13.ch013_t08_yr_own_while_else' + ("_ans" if is_answer else ""))

    def tearDown(self):
        del sys.modules[self.my_module.__name__]

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
