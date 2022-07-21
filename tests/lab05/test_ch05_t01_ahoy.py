import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab05/ch05_t01_ahoy.py")

        expected = "Pig Latin\n"
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
