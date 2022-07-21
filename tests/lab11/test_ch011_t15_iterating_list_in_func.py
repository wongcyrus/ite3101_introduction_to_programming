import unittest

from tests.unit_test_helper import is_answer




class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab11.ch011_t15_iterating_list_in_func_ans import total, n
        else:
            from lab.lab11.ch011_t15_iterating_list_in_func import total, n
        self.assertEqual(15, total([3, 5, 7]))
        self.assertEqual(sum(n), total(n))


if __name__ == '__main__':
    unittest.main()
