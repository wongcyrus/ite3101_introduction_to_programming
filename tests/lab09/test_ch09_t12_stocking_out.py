import unittest
from ..console_test_helper import is_answer

if is_answer:
    from lab.lab09.ch09_t12_stocking_out_ans import compute_bill
else:
    from lab.lab09.ch09_t12_stocking_out import compute_bill


class TestOutput(unittest.TestCase):

    def test(self):
        self.assertEqual(5.5, compute_bill(["banana", "orange", "apple"]))
        self.assertEqual(5.5, compute_bill(["banana", "orange"]))
        self.assertEqual(0, compute_bill([]))


if __name__ == '__main__':
    unittest.main()
