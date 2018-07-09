import unittest
from unit_test_helper import is_answer

if is_answer:
    from lab09.ch09_t06_your_own_score_ans import prices
else:
    from lab09.ch09_t06_your_own_score import prices


class TestOutput(unittest.TestCase):

    def test(self):
        self.assertDictEqual({
            "banana": 4,
            "apple": 2,
            "orange": 1.5,
            "pear": 3
        }, prices)


if __name__ == '__main__':
    unittest.main()
