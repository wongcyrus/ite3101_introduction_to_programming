import types
import unittest
from test.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def testFunctionDefined(self):
        temp_globals, temp_locals, content, output = execfile("lab06/ch06_t04_para_n_argu.py")
        print(temp_locals)
        self.assertIsInstance(temp_locals['power'], types.FunctionType)
        self.assertEqual(100000000000000000000, temp_locals['power'](10, 20))

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab06/ch06_t04_para_n_argu.py")
        print(output)
        expected = "37 to the power of 4 is 1874161.\n"
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
