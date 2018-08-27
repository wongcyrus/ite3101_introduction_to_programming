import unittest
from ..console_test_helper import *
from ..console_test_helper import is_answer

if is_answer:
    from lab.lab15.ch015_t04_compute_avg_ans import *
else:
    from lab.lab15.ch015_t04_compute_avg import *


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
