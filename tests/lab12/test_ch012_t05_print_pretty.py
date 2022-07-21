import unittest

from tests.unit_test_helper import is_answer
from tests.unit_test_helper.console_test_helper import get_function_output




class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab12.ch012_t05_print_pretty_ans import board
        else:
            from lab.lab12.ch012_t05_print_pretty import board
        self.assertIsInstance(board, type([]))
        expected = [['O', 'O', 'O', 'O', 'O'],
                    ['O', 'O', 'O', 'O', 'O'],
                    ['O', 'O', 'O', 'O', 'O'],
                    ['O', 'O', 'O', 'O', 'O'],
                    ['O', 'O', 'O', 'O', 'O']]
        self.assertListEqual(expected, board)

    def testOutput(self):
        if is_answer:
            from lab.lab12.ch012_t05_print_pretty_ans import board, print_board
        else:
            from lab.lab12.ch012_t05_print_pretty import board, print_board
        output, value = get_function_output(lambda: print_board(board))
        expected = """O O O O O
O O O O O
O O O O O
O O O O O
O O O O O
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
