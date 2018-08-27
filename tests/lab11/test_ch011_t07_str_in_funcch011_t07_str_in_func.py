import unittest

from ..console_test_helper import execfile, is_answer

if is_answer:
    from lab.lab11.ch011_t07_str_in_func_ans import string_function
else:
    from lab.lab11.ch011_t07_str_in_func import string_function


class TestOutput(unittest.TestCase):

    def test(self):
        self.assertEqual("Helloworld", string_function("Hello"))
        self.assertEqual("aworld", string_function("a"))

    def testOutput(self):
        temp_globals, temp_locals, content, output = execfile("lab11/ch011_t07_str_in_func.py")

        expected = """Helloworld
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
