import filecmp
import os
import unittest
from io import TextIOWrapper

from unit_test_helper import is_answer

if is_answer:
    from lab20.ch20_t08_try_it_yrself_ans import my_file
else:
    from lab20.ch20_t08_try_it_yrself import my_file


class TestOutput(unittest.TestCase):

    def setUp(self):
        self.filename = "ch20_t08o_output.txt"

    def tearDown(self):
        if os.path.isfile(self.filename):
            os.remove(self.filename)

    def test(self):
        self.assertIsInstance(my_file, TextIOWrapper)
        self.assertTrue(filecmp.cmp(self.filename, "output/ch20_t08o_output_ans.txt"))


if __name__ == '__main__':
    unittest.main()
