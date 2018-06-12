import unittest
from test.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content = execfile("lab01/ch01_t07_updating_variables.py")
        print(temp_locals)
        self.assertEqual(temp_locals['annual_rainfall'], 45.209999999999994)


if __name__ == '__main__':
    unittest.main()
