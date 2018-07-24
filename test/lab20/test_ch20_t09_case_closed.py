import filecmp
import os
import unittest
from io import TextIOWrapper

from unit_test_helper import is_answer
from unit_test_helper.console_test_helper import execfile

if is_answer:
    from lab20.ch20_t09_case_closed_ans import my_file
else:
    from lab20.ch20_t09_case_closed import my_file


class TestOutput(unittest.TestCase):

    def setUp(self):
        self.filename = "ch20_t09o_output.txt"

    def tearDown(self):
        if os.path.isfile(self.filename):
            os.remove(self.filename)

    def test(self):
        self.assertIsInstance(my_file, TextIOWrapper)
        self.assertTrue(filecmp.cmp(self.filename, "output/ch20_t09o_output_ans.txt"))

    def test_output(self):
        temp_globals, temp_locals, content, output = execfile("lab20/ch20_t09_case_closed.py")

        expected = f"""True
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
