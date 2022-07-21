import unittest

from tests.unit_test_helper import is_answer
from tests.unit_test_helper.console_test_helper import execfile




class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab11.ch011_t16_str_in_list_in_func_ans import join_strings, n
        else:
            from lab.lab11.ch011_t16_str_in_list_in_func import join_strings, n
        self.assertEqual("MichaelLieberman", join_strings(n))
        self.assertEqual("abc", join_strings(["a", "b", "c"]))

    def testOutput(self):
        temp_globals, temp_locals, content, output = execfile("lab11/ch011_t16_str_in_list_in_func.py")

        expected = """MichaelLieberman
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
