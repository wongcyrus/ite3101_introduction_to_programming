import types
import unittest
from tests.unit_test_helper.console_test_helper import *
from tests.unit_test_helper import is_answer




class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab07.ch07_t02_planning_your_trip_ans import hotel_cost
        else:
            from lab.lab07.ch07_t02_planning_your_trip import hotel_cost
        temp_globals, temp_locals, content, output = execfile("lab07/ch07_t02_planning_your_trip.py")
        print(temp_locals)
        self.assertIsInstance(temp_locals['hotel_cost'], types.FunctionType)
        self.assertEqual(140, hotel_cost(1))
        self.assertEqual(1400, hotel_cost(10))


if __name__ == '__main__':
    unittest.main()
