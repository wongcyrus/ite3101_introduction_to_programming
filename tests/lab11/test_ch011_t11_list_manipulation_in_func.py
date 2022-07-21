import unittest

from tests.unit_test_helper import is_answer
from tests.unit_test_helper.console_test_helper import execfile




class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab11.ch011_t11_list_manipulation_in_func_ans import list_extender, n
        else:
            from lab.lab11.ch011_t11_list_manipulation_in_func import list_extender, n
        self.assertListEqual([3, 5, 7, 9], list_extender([3, 5, 7]))
        self.assertListEqual([3, 5, 7, 9, 9], list_extender(n))

    def testOutput(self):
        temp_globals, temp_locals, content, output = execfile("lab11/ch011_t11_list_manipulation_in_func.py")

        expected = """[3, 5, 7, 9]
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
