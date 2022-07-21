import unittest

from unittest.mock import patch

from tests.unit_test_helper import is_answer
from tests.unit_test_helper.console_test_helper import get_function_output


class TestOutput(unittest.TestCase):

    @patch("builtins.input", side_effect=["1", "2"])
    def test(self, mock_input):
        def load():
            if is_answer:
                from lab.lab12.ch012_t08_it_is_debugging_ans import ship_row, ship_col
            else:
                from lab.lab12.ch012_t08_it_is_debugging import ship_row, ship_col
            return f"""{ship_row}
{ship_col}
"""

        output, value = get_function_output(load)
        self.assertEqual(output, value)


if __name__ == '__main__':
    unittest.main()
