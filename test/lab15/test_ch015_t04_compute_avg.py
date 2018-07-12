import unittest
from test.unit_test_helper.console_test_helper import *

if is_answer:
    from lab15.ch015_t04_compute_avg_ans import *
else:
    from lab15.ch015_t04_compute_avg import *


class TestOutput(unittest.TestCase):

    def test(self):
        self.assertAlmostEqual(80.42307692307692, grades_average(grades))

    def test_output(self):
        temp_globals, temp_locals, content, output = execfile("lab15/ch015_t04_compute_avg.py", globals())
        avg = grades_average(grades)
        expect = f"""{avg}
"""
        self.assertEqual(expect, output)


if __name__ == '__main__':
    unittest.main()
