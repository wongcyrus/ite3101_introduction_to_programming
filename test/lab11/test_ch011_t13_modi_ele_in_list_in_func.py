import unittest

from unit_test_helper import is_answer
from unit_test_helper.console_test_helper import execfile

if is_answer:
    from lab11.ch011_t13_modi_ele_in_list_in_func_ans import double_list, n
else:
    from lab11.ch011_t13_modi_ele_in_list_in_func import double_list, n


class TestOutput(unittest.TestCase):

    def test(self):
        self.assertListEqual([6, 10, 14], double_list([3, 5, 7]))
        self.assertListEqual([24, 40, 56], double_list(n))

    def testOutput(self):
        temp_globals, temp_locals, content, output = execfile("lab11/ch011_t13_modi_ele_in_list_in_func.py")

        expected = """[12, 20, 28]
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
