import unittest
from tests.unit_test_helper import is_answer




class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab14.ch014_t11_purify_ans import purify
        else:
            from lab.lab14.ch014_t11_purify import purify
        self.assertListEqual([2], purify([1, 2, 1, 1]))
        self.assertListEqual([2, 2, 2, 2], purify([2, 2, 2, 2]))
        self.assertListEqual([], purify([1, 1, 1, 1]))
        self.assertListEqual([], purify([]))


if __name__ == '__main__':
    unittest.main()
