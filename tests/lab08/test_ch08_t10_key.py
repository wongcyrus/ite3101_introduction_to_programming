import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab08/ch08_t10_key.py")

        expected = """104
105
106
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
