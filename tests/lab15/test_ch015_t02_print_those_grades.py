import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab15/ch015_t02_print_those_grades.py")
        expect = """100
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
"""
        self.assertEqual(expect, output)


if __name__ == '__main__':
    unittest.main()
