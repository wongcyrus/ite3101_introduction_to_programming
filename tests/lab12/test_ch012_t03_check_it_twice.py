import unittest

from ..console_test_helper import execfile, is_answer

if is_answer:
    from lab.lab12.ch012_t03_check_it_twice_ans import board
else:
    from lab.lab12.ch012_t03_check_it_twice import board


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
        temp_globals, temp_locals, content, output = execfile("lab12/ch012_t03_check_it_twice.py")

        expected = """[['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']]
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
