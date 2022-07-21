import types
import unittest
from tests.unit_test_helper.console_test_helper import execfile
from tests.unit_test_helper import is_answer




class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab07.ch07_t07_plan_your_trip_ans import trip_cost
        else:
            from lab.lab07.ch07_t07_plan_your_trip import trip_cost
        temp_globals, temp_locals, content, output = execfile("lab07/ch07_t07_plan_your_trip.py", globals())

        print(temp_locals)
        self.assertIsInstance(temp_locals['trip_cost'], types.FunctionType)
        self.assertEqual(1815, trip_cost("Los Angeles", 5, 600))
        self.assertEqual("1815\n", output)


if __name__ == '__main__':
    unittest.main()
