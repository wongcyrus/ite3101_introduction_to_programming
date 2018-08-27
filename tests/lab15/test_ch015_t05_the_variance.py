import unittest
from ..console_test_helper import *
from ..console_test_helper import is_answer

if is_answer:
    from lab.lab15.ch015_t05_the_variance_ans import *
else:
    from lab.lab15.ch015_t05_the_variance import *


class TestOutput(unittest.TestCase):

    def test(self):
        self.assertAlmostEqual(334.0710059171598, grades_variance(grades))

    def test_output(self):
        temp_globals, temp_locals, content, output = execfile("lab15/ch015_t05_the_variance.py", globals())
        var = grades_variance(grades)
        expect = f"""{var}
"""
        self.assertEqual(expect, output)


if __name__ == '__main__':
    unittest.main()
