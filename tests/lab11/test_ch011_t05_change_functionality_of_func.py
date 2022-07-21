import unittest

from tests.unit_test_helper import is_answer
from tests.unit_test_helper.console_test_helper import execfile

if is_answer:
    from lab.lab11.ch011_t05_change_functionality_of_func_ans import my_function, number
else:
    from lab.lab11.ch011_t05_change_functionality_of_func import my_function, number


class TestOutput(unittest.TestCase):

    def test(self):
        self.assertEqual(15, my_function(number))

    def testOutput(self):
        temp_globals, temp_locals, content, output = execfile("lab11/ch011_t05_change_functionality_of_func.py")

        expected = """15
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
