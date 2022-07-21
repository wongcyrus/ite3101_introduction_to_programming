import types
import unittest
from tests.unit_test_helper.console_test_helper import *
from tests.unit_test_helper import is_answer




class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab07.ch07_t04_transportation_ans import rental_car_cost
        else:
            from lab.lab07.ch07_t04_transportation import rental_car_cost
        temp_globals, temp_locals, content, output = execfile("lab07/ch07_t04_transportation.py")
        print(temp_locals)
        self.assertIsInstance(temp_locals['rental_car_cost'], types.FunctionType)
        self.assertEqual(40, rental_car_cost(1))
        self.assertEqual(100, rental_car_cost(3))
        self.assertEqual(230, rental_car_cost(7))
        self.assertEqual(350, rental_car_cost(10))


if __name__ == '__main__':
    unittest.main()
