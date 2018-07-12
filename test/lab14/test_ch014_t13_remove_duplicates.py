import unittest
from unit_test_helper import is_answer

if is_answer:
    from lab14.ch014_t13_remove_duplicates_ans import remove_duplicates
else:
    from lab14.ch014_t13_remove_duplicates import remove_duplicates


class TestOutput(unittest.TestCase):

    def test(self):
        self.assertListEqual([1, 2], remove_duplicates([1, 2, 1, 1]))
        self.assertListEqual([2], remove_duplicates([2, 2, 2, 2]))
        self.assertListEqual([1], remove_duplicates([1, 1, 1, 1]))
        self.assertListEqual([], remove_duplicates([]))


if __name__ == '__main__':
    unittest.main()
