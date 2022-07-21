import unittest
from tests.unit_test_helper import is_answer




class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab14.ch014_t12_product_ans import product
        else:
            from lab.lab14.ch014_t12_product import product
        self.assertEqual(2, product([1, 2, 1, 1]))
        self.assertEqual(16, product([2, 2, 2, 2]))
        self.assertEqual(1, product([1, 1, 1, 1]))
        self.assertEqual(0, product([0, 1, 1, 1]))
        self.assertEqual(1, product([]))


if __name__ == '__main__':
    unittest.main()
