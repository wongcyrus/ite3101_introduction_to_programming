import unittest
from test.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab05/ch05_t01_ahoy.py")
        print(output)
        expected = "Pig Latin\n"
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
