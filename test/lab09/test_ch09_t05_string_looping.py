import unittest
from test.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab09/ch09_t05_string_looping.py")
        print(output)
        expected = """C
o
d
e
c
a
d
e
m
y


i
i
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
