import unittest
from test.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab09/ch09_t02_this_is_key.py")
        print(output)
        expected = """A star of a popular children's cartoon show.
The sound a goat makes.
Goes on the floor.
A small amount.
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
