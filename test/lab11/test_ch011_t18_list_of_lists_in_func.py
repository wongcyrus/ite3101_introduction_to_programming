import unittest

from unit_test_helper import is_answer
from unit_test_helper.console_test_helper import execfile

if is_answer:
    from lab11.ch011_t18_list_of_lists_in_func_ans import flatten, n
else:
    from lab11.ch011_t18_list_of_lists_in_func import flatten, n


class TestOutput(unittest.TestCase):

    def test(self):
        self.assertListEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], flatten(n))
        self.assertListEqual([1, 2, 5, 6], flatten([[1, 2], [5, 6]]))

    def testOutput(self):
        temp_globals, temp_locals, content, output = execfile("lab11/ch011_t17_two_lists_two_argu_in_func.py")

        expected = """[1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
