import unittest
from tests.unit_test_helper import is_answer




class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab09.ch09_t11_making_a_purchase_ans import compute_bill
        else:
            from lab.lab09.ch09_t11_making_a_purchase import compute_bill
        self.assertEqual(7.5, compute_bill(["banana", "orange", "apple"]))
        self.assertEqual(5.5, compute_bill(["banana", "orange"]))
        self.assertEqual(0, compute_bill([]))


if __name__ == '__main__':
    unittest.main()
