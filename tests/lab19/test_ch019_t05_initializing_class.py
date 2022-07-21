import unittest
from tests.unit_test_helper import is_answer




class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab19.ch019_t05_initializing_class_ans import Car, my_car
        else:
            from lab.lab19.ch019_t05_initializing_class import Car, my_car
        self.assertIsInstance(my_car, Car)
        self.assertEqual("new", my_car.condition)
        self.assertEqual("DeLorean", my_car.model)
        self.assertEqual("silver", my_car.color)
        self.assertEqual(88, my_car.mpg)


if __name__ == '__main__':
    unittest.main()
