import unittest

from test.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab06/ch06_t18_review_modules.py")
        print(output)
        self.assertEqual("117.0\n", output)


if __name__ == '__main__':
    unittest.main()
