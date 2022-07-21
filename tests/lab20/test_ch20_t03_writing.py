import os
import unittest
from io import TextIOWrapper

from tests.unit_test_helper import is_answer


class TestOutput(unittest.TestCase):

    def setUp(self):
        self.filename = os.path.join(os.path.dirname(
            __file__), "..", "..", "lab/lab20/outputs/ch20_t03_output.txt")

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
        if is_answer:
            from lab.lab20.ch20_t03_writing_ans import my_file
        else:
            from lab.lab20.ch20_t03_writing import my_file

        self.assertIsInstance(my_file, TextIOWrapper)
        file_path_name = os.path.join(os.path.dirname(
            __file__), "output/ch20_t03o_output_ans.txt")
        self.assertTrue(self.cmp_lines(self.filename, file_path_name))


if __name__ == '__main__':
    unittest.main()
