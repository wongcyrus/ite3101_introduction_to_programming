import unittest
from tests.unit_test_helper import is_answer




class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab14.ch014_t10_count_ans import count
        else:
            from lab.lab14.ch014_t10_count import count
        self.assertEqual(3, count([1, 2, 1, 1], 1))
        self.assertEqual(0, count([], 1))


if __name__ == '__main__':
    unittest.main()
