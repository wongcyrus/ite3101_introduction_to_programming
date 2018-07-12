import unittest
from test.unit_test_helper.console_test_helper import *

if is_answer:
    from lab15.ch015_t07_review_ans import *
else:
    from lab15.ch015_t07_review import *


class TestOutput(unittest.TestCase):

    def test(self):
        self.assertAlmostEqual(18.277609414722697, grades_std_deviation(grades_variance(grades)))

    def test_output(self):
        temp_globals, temp_locals, content, output = execfile("lab15/ch015_t07_review.py", globals())
        avg = grades_average(grades)
        var = grades_variance(grades)
        std = grades_std_deviation(grades_variance(grades))
        expect = f"""100
100
90
40
80
100
85
70
90
65
90
85
50.5
1045.5
{avg}
{var}
{std}
"""
        self.assertEqual(expect, output)


if __name__ == '__main__':
    unittest.main()
