import types
import unittest
from tests.unit_test_helper.console_test_helper import *
from tests.unit_test_helper import is_answer



class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab06.ch06_t05_func_calling_func_ans import deserves_another
        else:
            from lab.lab06.ch06_t05_func_calling_func import deserves_another

        temp_globals, temp_locals, content, output = execfile("lab06/ch06_t05_func_calling_func.py")
        print(temp_locals)
        self.assertIsInstance(temp_locals['one_good_turn'], types.FunctionType)
        self.assertIsInstance(temp_locals['deserves_another'], types.FunctionType)
        self.assertEqual(11, temp_locals['one_good_turn'](10))
        self.assertEqual(13, deserves_another(10))


if __name__ == '__main__':
    unittest.main()
