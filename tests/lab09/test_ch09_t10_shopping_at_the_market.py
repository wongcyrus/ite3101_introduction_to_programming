import unittest
from ..console_test_helper import is_answer

if is_answer:
    from lab.lab09.ch09_t10_shopping_at_the_market_ans import groceries
else:
    from lab.lab09.ch09_t10_shopping_at_the_market import groceries


class TestOutput(unittest.TestCase):

    def test(self):
        self.assertListEqual(["banana", "orange", "apple"], groceries)


if __name__ == '__main__':
    unittest.main()
