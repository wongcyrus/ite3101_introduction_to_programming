import types
import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def testFunctionDefined(self):
        temp_globals, temp_locals, content, output = execfile("lab06/ch06_t03_call_n_response.py")
        print(temp_locals)
        self.assertIsInstance(temp_locals['square'], types.FunctionType)
        self.assertEqual(100, temp_locals['square'](10))

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab06/ch06_t03_call_n_response.py")

        expected = "10 squared is 100.\n"
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
