import unittest

from tests.unit_test_helper import is_answer
from tests.unit_test_helper.console_test_helper import execfile



class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab11.ch011_t17_two_lists_two_argu_in_func_ans import join_lists, n, m
        else:
            from lab.lab11.ch011_t17_two_lists_two_argu_in_func import join_lists, n, m
        self.assertListEqual([1, 2, 3, 4, 5, 6], join_lists(m, n))
        self.assertListEqual([1, 2, 5, 6], join_lists([1, 2], [5, 6]))

    def testOutput(self):
        temp_globals, temp_locals, content, output = execfile("lab11/ch011_t17_two_lists_two_argu_in_func.py")

        expected = """[1, 2, 3, 4, 5, 6]
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
