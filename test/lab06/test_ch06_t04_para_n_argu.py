import types
import unittest
from test.unit_test_helper.console_test_helper import *

if is_answer:
    from lab06.ch06_t04_para_n_argu_ans import power
else:
    from lab06.ch06_t04_para_n_argu import power


class TestOutput(unittest.TestCase):

    def testFunctionDefined(self):
        temp_globals, temp_locals, content, output = execfile("lab06/ch06_t04_para_n_argu.py")
        print(temp_locals)
        self.assertIsInstance(temp_locals['power'], types.FunctionType)
        self.assertEqual(None, power(10, 20))

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab06/ch06_t04_para_n_argu.py")

        expected = "37 to the power of 4 is 1874161.\n"
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
