import unittest

from tests.unit_test_helper import is_answer
from tests.unit_test_helper.console_test_helper import execfile




class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab11.ch011_t07_str_in_func_ans import string_function
        else:
            from lab.lab11.ch011_t07_str_in_func import string_function
        self.assertEqual("Helloworld", string_function("Hello"))
        self.assertEqual("aworld", string_function("a"))

    def testOutput(self):
        temp_globals, temp_locals, content, output = execfile("lab11/ch011_t07_str_in_func.py")

        expected = """Helloworld
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
