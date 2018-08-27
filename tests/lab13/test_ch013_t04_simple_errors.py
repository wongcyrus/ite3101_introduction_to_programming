import sys
import unittest
from unittest.mock import patch

from ..console_test_helper import get_function_output, is_answer
from ..timeout import timeout


class TestOutput(unittest.TestCase):

    def load(self):
        self.myModule = __import__('lab13.ch013_t04_simple_errors' + "_ans" if is_answer else "", globals(),
                                   locals(),
                                   [''], 0)

    def tearDown(self):
        del sys.modules[self.myModule.__name__]
        return

    @timeout(1)
    @patch("builtins.input", side_effect=["y"])
    @patch("random.randint", lambda x, y: 1)
    def test_y(self, mock_input):
        output, value = get_function_output(lambda: self.load())
        expect = ""
        self.assertEqual(expect, output)

    @timeout(1)
    @patch("builtins.input", side_effect=["n"])
    @patch("random.randint", lambda x, y: 1)
    def test_n(self, mock_input):
        output, value = get_function_output(lambda: self.load())
        expect = ""
        self.assertEqual(expect, output)

    @timeout(1)
    @patch("builtins.input", side_effect=["x", "n"])
    @patch("random.randint", lambda x, y: 1)
    def test_n(self, mock_input):
        output, value = get_function_output(lambda: self.load())
        expect = ""
        self.assertEqual(expect, output)


if __name__ == '__main__':
    unittest.main()
