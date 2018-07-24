import unittest
from io import TextIOWrapper

from unit_test_helper import is_answer

if is_answer:
    from lab20.ch20_t02_open_func_ans import my_file
else:
    from lab20.ch20_t02_open_func import my_file


class TestOutput(unittest.TestCase):

    def test(self):
        self.assertIsInstance(my_file, TextIOWrapper)


if __name__ == '__main__':
    unittest.main()
