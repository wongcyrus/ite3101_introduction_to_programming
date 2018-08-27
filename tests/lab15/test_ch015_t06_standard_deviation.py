import unittest
from ..console_test_helper import *
from ..console_test_helper import is_answer

if is_answer:
    from lab.lab15.ch015_t06_standard_deviation_ans import *
else:
    from lab.lab15.ch015_t06_standard_deviation import *


class TestOutput(unittest.TestCase):

    def test(self):
        self.assertAlmostEqual(18.277609414722697, grades_std_deviation(grades_variance(grades)))

    def test_output(self):
        temp_globals, temp_locals, content, output = execfile("lab15/ch015_t06_standard_deviation.py", globals())
        std = grades_std_deviation(grades_variance(grades))
        expect = f"""{std}
"""
        self.assertEqual(expect, output)


if __name__ == '__main__':
    unittest.main()
