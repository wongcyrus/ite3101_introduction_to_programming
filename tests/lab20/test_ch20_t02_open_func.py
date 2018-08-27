import unittest
from io import TextIOWrapper
import os

from ..console_test_helper import is_answer

os.chdir(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../lab/lab20'))
if is_answer:
    from lab.lab20.ch20_t02_open_func_ans import my_file
else:
    from lab.lab20.ch20_t02_open_func import my_file


class TestOutput(unittest.TestCase):

    def test(self):
        self.assertIsInstance(my_file, TextIOWrapper)


if __name__ == '__main__':
    unittest.main()
