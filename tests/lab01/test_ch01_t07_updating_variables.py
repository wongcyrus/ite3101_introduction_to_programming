import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab01/ch01_t07_updating_variables.py")
        print(temp_locals)
        self.assertAlmostEqual(45.209999999999994, temp_locals['annual_rainfall'])


if __name__ == '__main__':
    unittest.main()
