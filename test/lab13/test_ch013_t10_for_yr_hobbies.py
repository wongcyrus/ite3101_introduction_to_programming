import sys
import unittest
from unittest.mock import patch

from unit_test_helper import is_answer
from unit_test_helper.console_test_helper import get_function_output
from unit_test_helper.timeout import timeout


class TestOutput(unittest.TestCase):

    def load(self):
        self.myModule = __import__('lab13.ch013_t10_for_yr_hobbies' + "_ans" if is_answer else "", globals(), locals(),
                                   [''], 0)
        if is_answer:
            from lab13.ch013_t10_for_yr_hobbies_ans import hobbies
        else:
            from lab13.ch013_t10_for_yr_hobbies import hobbies
        return hobbies

    def tearDown(self):
        del sys.modules[self.myModule.__name__]
        return

    @timeout(1)
    @patch("builtins.input", side_effect=["swimming", "running", "football"])
    def test(self, mock_input):
        output, value = get_function_output(lambda: self.load())
        expect = ['swimming', 'running', 'football']
        self.assertListEqual(expect, value)


if __name__ == '__main__':
    unittest.main()
