import unittest
from tests.unit_test_helper.console_test_helper import *




class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab15.ch015_t05_the_variance_ans import grades_variance, grades
        else:
            from lab.lab15.ch015_t05_the_variance import grades_variance, grades
        self.assertAlmostEqual(334.0710059171598, grades_variance(grades))

    def test_output(self):
        if is_answer:
            from lab.lab15.ch015_t05_the_variance_ans import grades_variance, grades
        else:
            from lab.lab15.ch015_t05_the_variance import grades_variance, grades
        temp_globals, temp_locals, content, output = execfile("lab15/ch015_t05_the_variance.py", globals())
        var = grades_variance(grades)
        expect = f"""{var}
"""
        self.assertEqual(expect, output)


if __name__ == '__main__':
    unittest.main()
