import unittest
from tests.unit_test_helper import is_answer



class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab14.ch014_t14_median_ans import median
        else:
            from lab.lab14.ch014_t14_median import median

        self.assertEqual(1, median([1, 1, 2]))
        self.assertEqual(1, median([1, 2, 1]))
        self.assertEqual(1, median([1, 2, 1, 1]))
        self.assertEqual(2, median([2, 2, 2, 2]))
        self.assertEqual(1, median([1, 1, 1, 1]))
        self.assertEqual(2.5, median([1, 2, 3, 4]))
        self.assertEqual(2, median([1, 2, 3]))


if __name__ == '__main__':
    unittest.main()
