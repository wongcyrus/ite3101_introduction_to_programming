import unittest
from tests.unit_test_helper import is_answer




class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab09.ch09_t04_lists_n_functions_ans import fizz_count
        else:
            from lab.lab09.ch09_t04_lists_n_functions import fizz_count
        self.assertEqual(2, fizz_count(["fizz", "cat", "fizz"]))
        self.assertEqual(0, fizz_count(["fzz", "cat", "fzz"]))


if __name__ == '__main__':
    unittest.main()
