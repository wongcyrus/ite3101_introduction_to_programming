# ch012_t06_hide
import unittest

from unit_test_helper import is_answer

if is_answer:
    from lab12.ch012_t06_hide_ans import board, random_row, random_col
else:
    from lab12.ch012_t06_hide import board, random_row, random_col


class TestOutput(unittest.TestCase):

    def test(self):
        self.assertIsInstance(board, type([]))
        expected = [['O', 'O', 'O', 'O', 'O'],
                    ['O', 'O', 'O', 'O', 'O'],
                    ['O', 'O', 'O', 'O', 'O'],
                    ['O', 'O', 'O', 'O', 'O'],
                    ['O', 'O', 'O', 'O', 'O']]
        self.assertListEqual(expected, board)

    def testRandom(self):
        for i in range(0, 100):
            self.assertIn(random_row(board), range(0, 5))
            self.assertIn(random_col(board), range(0, 5))


if __name__ == '__main__':
    unittest.main()
