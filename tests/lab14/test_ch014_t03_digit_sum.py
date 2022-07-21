import unittest
from tests.unit_test_helper import is_answer




class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab14.ch014_t03_digit_sum_ans import digit_sum
        else:
            from lab.lab14.ch014_t03_digit_sum import digit_sum
        self.assertEqual(1, digit_sum(10))
        self.assertEqual(2, digit_sum(11))
        self.assertEqual(3, digit_sum(12))
        self.assertEqual(5, digit_sum(131))
        self.assertEqual(0, digit_sum(0))


if __name__ == '__main__':
    unittest.main()
