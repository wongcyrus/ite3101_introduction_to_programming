import unittest

from ..console_test_helper import get_function_output, is_answer

if is_answer:
    from lab.lab12.ch012_t04_custom_print_ans import board, print_board
else:
    from lab.lab12.ch012_t04_custom_print import board, print_board


class TestOutput(unittest.TestCase):

    def test(self):
        self.assertIsInstance(board, type([]))
        expected = [['O', 'O', 'O', 'O', 'O'],
                    ['O', 'O', 'O', 'O', 'O'],
                    ['O', 'O', 'O', 'O', 'O'],
                    ['O', 'O', 'O', 'O', 'O'],
                    ['O', 'O', 'O', 'O', 'O']]
        self.assertListEqual(expected, board)

    def testOutput(self):
        output, value = get_function_output(lambda: print_board(board))
        expected = """['O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O']
['O', 'O', 'O', 'O', 'O']
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
