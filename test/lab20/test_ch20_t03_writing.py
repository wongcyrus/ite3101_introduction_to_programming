import filecmp
import os
import unittest
from io import TextIOWrapper

from unit_test_helper import is_answer

if is_answer:
    from lab20.ch20_t03_writing_ans import my_file
else:
    from lab20.ch20_t03_writing import my_file


class TestOutput(unittest.TestCase):

    def setUp(self):
        self.filename = "ch20_t03_output.txt"

    def tearDown(self):
        if os.path.isfile(self.filename):
            os.remove(self.filename)

    @staticmethod
    def cmp_lines(path_1: str, path_2: str):
        l1 = l2 = ' '
        with open(path_1, 'r') as f1, open(path_2, 'r') as f2:
            while l1 != '' and l2 != '':
                l1 = f1.readline()
                l2 = f2.readline()
                if l1 != l2:
                    return False
        return True

    def test(self):
        self.assertIsInstance(my_file, TextIOWrapper)
        self.assertTrue(self.cmp_lines(self.filename, "output/ch20_t03o_output_ans.txt"))


if __name__ == '__main__':
    unittest.main()
