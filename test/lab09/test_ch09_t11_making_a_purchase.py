import unittest
from unit_test_helper import is_answer

if is_answer:
    from lab09.ch09_t11_making_a_purchase_ans import compute_bill
else:
    from lab09.ch09_t11_making_a_purchase import compute_bill


class TestOutput(unittest.TestCase):

    def test(self):
        self.assertEqual(7.5, compute_bill(["banana", "orange", "apple"]))
        self.assertEqual(5.5, compute_bill(["banana", "orange"]))
        self.assertEqual(0, compute_bill([]))


if __name__ == '__main__':
    unittest.main()
