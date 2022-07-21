import filecmp
import os
import unittest
from io import TextIOWrapper

from tests.unit_test_helper import is_answer




class TestOutput(unittest.TestCase):

    def setUp(self):
        self.filename = os.path.join(os.path.dirname(__file__),"..","..","lab/lab20/outputs/ch20_t08o_output.txt" )

    def tearDown(self):
        if os.path.isfile(self.filename):
            os.remove(self.filename)

    def test(self):
        if is_answer:
            from lab.lab20.ch20_t08_try_it_yrself_ans import my_file
        else:
            from lab.lab20.ch20_t08_try_it_yrself import my_file
        self.assertIsInstance(my_file, TextIOWrapper)
        file_path_name = os.path.join(os.path.dirname(__file__),"output/ch20_t08o_output_ans.txt")
        self.assertTrue(filecmp.cmp(self.filename, file_path_name))


if __name__ == '__main__':
    unittest.main()
