import unittest

from unit_test_helper import is_answer
from unit_test_helper.console_test_helper import execfile

if is_answer:
    from lab11.ch011_t09_use_ele_from_list_in_func_ans import list_function, n
else:
    from lab11.ch011_t09_use_ele_from_list_in_func import list_function, n


class TestOutput(unittest.TestCase):

    def test(self):
        self.assertEqual(5, list_function(n))

    def testOutput(self):
        temp_globals, temp_locals, content, output = execfile("lab11/ch011_t09_use_ele_from_list_in_func.py")

        expected = """5
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
