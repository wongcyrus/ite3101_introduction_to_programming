import unittest
from tests.unit_test_helper import is_answer




class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab09.ch09_t07_investing_in_stock_ans import stock
        else:
            from lab.lab09.ch09_t07_investing_in_stock import stock
        self.assertDictEqual({
            "banana": 6,
            "apple": 0,
            "orange": 32,
            "pear": 15,
        }, stock)


if __name__ == '__main__':
    unittest.main()
