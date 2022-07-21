import unittest

from tests.unit_test_helper import is_answer




class TestOutput(unittest.TestCase):


    def test(self):
        if is_answer:
            from lab.lab12.ch012_t06_hide_ans import board, random_row, random_col
        else:
            from lab.lab12.ch012_t06_hide import board, random_row, random_col
        self.assertIsInstance(board, type([]))
        expected = [['O', 'O', 'O', 'O', 'O'],
                    ['O', 'O', 'O', 'O', 'O'],
                    ['O', 'O', 'O', 'O', 'O'],
                    ['O', 'O', 'O', 'O', 'O'],
                    ['O', 'O', 'O', 'O', 'O']]
        self.assertListEqual(expected, board)

    def testRandom(self):
        if is_answer:
            from lab.lab12.ch012_t06_hide_ans import board, random_row, random_col
        else:
            from lab.lab12.ch012_t06_hide import board, random_row, random_col
        for i in range(0, 100):
            self.assertIn(random_row(board), range(0, 5))
            self.assertIn(random_col(board), range(0, 5))


if __name__ == '__main__':
    unittest.main()
