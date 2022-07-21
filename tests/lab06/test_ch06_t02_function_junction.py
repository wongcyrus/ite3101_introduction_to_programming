import types
import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def testFunctionDefined(self):
        temp_globals, temp_locals, content, output = execfile("lab06/ch06_t02_function_junction.py")
        print(temp_locals)
        self.assertIsInstance(temp_locals['spam'], types.FunctionType)

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab06/ch06_t02_function_junction.py")

        expected = "Eggs!\n"
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
