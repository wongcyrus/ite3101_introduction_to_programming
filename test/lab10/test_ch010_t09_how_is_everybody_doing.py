import unittest
from unit_test_helper import is_answer
from unit_test_helper.console_test_helper import execfile

if is_answer:
    from lab10.ch010_t09_how_is_everybody_doing_ans import *
else:
    from lab10.ch010_t09_how_is_everybody_doing import *


class TestOutput(unittest.TestCase):

    def test(self):
        self.assertListEqual([alice, lloyd, tyler], students)
        self.assertAlmostEqual(83.86666666666666, get_class_average(students))

    def testOutput(self):
        temp_globals, temp_locals, content, output = execfile("lab10/ch010_t09_how_is_everybody_doing.py", globals())

        expected = """B
83.86666666666666
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
