import unittest
from tests.unit_test_helper import is_answer




class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab09.ch09_t10_shopping_at_the_market_ans import groceries
        else:
            from lab.lab09.ch09_t10_shopping_at_the_market import groceries
        self.assertListEqual(["banana", "orange", "apple"], groceries)


if __name__ == '__main__':
    unittest.main()
