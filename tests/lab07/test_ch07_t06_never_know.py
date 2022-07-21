import types
import unittest
from tests.unit_test_helper.console_test_helper import *
from tests.unit_test_helper import is_answer




class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab07.ch07_t06_never_know_ans import trip_cost
        else:
            from lab.lab07.ch07_t06_never_know import trip_cost
        temp_globals, temp_locals, content, output = execfile("lab07/ch07_t06_never_know.py")
        print(temp_locals)
        self.assertIsInstance(temp_locals['trip_cost'], types.FunctionType)
        self.assertEqual(233, trip_cost("Charlotte", 1, 10))
        self.assertEqual(625, trip_cost("Tampa", 3, 25))
        self.assertEqual(1322, trip_cost("Pittsburgh", 7, 30))
        self.assertEqual(2585, trip_cost("Los Angeles", 10, 500))


if __name__ == '__main__':
    unittest.main()
