import unittest

from tests.unit_test_helper import is_answer
from tests.unit_test_helper.console_test_helper import execfile




class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab11.ch011_t09_use_ele_from_list_in_func_ans import list_function, n
        else:
            from lab.lab11.ch011_t09_use_ele_from_list_in_func import list_function, n
        self.assertEqual(5, list_function(n))

    def testOutput(self):
        temp_globals, temp_locals, content, output = execfile("lab11/ch011_t09_use_ele_from_list_in_func.py")

        expected = """5
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
