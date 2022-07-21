import unittest

from tests.unit_test_helper import is_answer
from tests.unit_test_helper.console_test_helper import execfile



class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab12.ch012_t01_get_our_feet_wet_ans import board
        else:
            from lab.lab12.ch012_t01_get_our_feet_wet import board

        self.assertIsInstance(board, type([]))
        self.assertListEqual([], board)

    def testOutput(self):
        temp_globals, temp_locals, content, output = execfile("lab12/ch012_t01_get_our_feet_wet.py")

        expected = """"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
