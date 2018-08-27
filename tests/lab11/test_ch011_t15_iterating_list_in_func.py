import unittest

from ..console_test_helper import is_answer

if is_answer:
    from lab.lab11.ch011_t15_iterating_list_in_func_ans import total, n
else:
    from lab.lab11.ch011_t15_iterating_list_in_func import total, n


class TestOutput(unittest.TestCase):

    def test(self):
        self.assertEqual(15, total([3, 5, 7]))
        self.assertEqual(sum(n), total(n))


if __name__ == '__main__':
    unittest.main()
