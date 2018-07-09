import unittest

from unit_test_helper import is_answer
from unit_test_helper.console_test_helper import execfile

if is_answer:
    from lab11.ch011_t06_more_than_one_argu_ans import add_function
else:
    from lab11.ch011_t06_more_than_one_argu import add_function


class TestOutput(unittest.TestCase):

    def test(self):
        self.assertEqual(3, add_function(1, 2))
        self.assertEqual(7, add_function(3, 4))

    def testOutput(self):
        temp_globals, temp_locals, content, output = execfile("lab11/ch011_t06_more_than_one_argu.py")

        expected = """18
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
