import unittest
from tests.unit_test_helper.console_test_helper import *




class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab15.ch015_t06_standard_deviation_ans import grades_std_deviation,grades_variance,grades
        else:
            from lab.lab15.ch015_t06_standard_deviation import grades_std_deviation,grades_variance,grades
        self.assertAlmostEqual(18.277609414722697, grades_std_deviation(grades_variance(grades)))

    def test_output(self):
        if is_answer:
            from lab.lab15.ch015_t06_standard_deviation_ans import grades_std_deviation,grades_variance,grades
        else:
            from lab.lab15.ch015_t06_standard_deviation import grades_std_deviation,grades_variance,grades
        temp_globals, temp_locals, content, output = execfile("lab15/ch015_t06_standard_deviation.py", globals())
        std = grades_std_deviation(grades_variance(grades))
        expect = f"""{std}
"""
        self.assertEqual(expect, output)


if __name__ == '__main__':
    unittest.main()
