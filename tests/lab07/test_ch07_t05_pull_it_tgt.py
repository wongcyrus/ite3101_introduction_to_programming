import types
import unittest
from tests.unit_test_helper.console_test_helper import *
from tests.unit_test_helper import is_answer




class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab07.ch07_t05_pull_it_tgt_ans import trip_cost
        else:
            from lab.lab07.ch07_t05_pull_it_tgt import trip_cost
        temp_globals, temp_locals, content, output = execfile("lab07/ch07_t05_pull_it_tgt.py")
        print(temp_locals)
        self.assertIsInstance(temp_locals['trip_cost'], types.FunctionType)
        self.assertEqual(223, trip_cost("Charlotte", 1))
        self.assertEqual(600, trip_cost("Tampa", 3))
        self.assertEqual(1292, trip_cost("Pittsburgh", 7))
        self.assertEqual(2085, trip_cost("Los Angeles", 10))


if __name__ == '__main__':
    unittest.main()
