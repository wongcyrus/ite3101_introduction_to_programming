import types
import unittest
from tests.unit_test_helper.console_test_helper import *
from tests.unit_test_helper import is_answer



class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab06.ch06_t19_builtin_functions_ans import distance_from_zero
        else:
            from lab.lab06.ch06_t19_builtin_functions import distance_from_zero
        temp_globals, temp_locals, content, output = execfile("lab06/ch06_t19_builtin_functions.py")
        print(temp_locals)
        self.assertIsInstance(temp_locals['distance_from_zero'], types.FunctionType)
        self.assertEqual("Nope", distance_from_zero("yes"))
        self.assertEqual(1, distance_from_zero(1))
        self.assertEqual(1.0, distance_from_zero(1.0))
        self.assertEqual(1, distance_from_zero(-1))
        self.assertEqual(1.0, distance_from_zero(-1.0))


if __name__ == '__main__':
    unittest.main()
