import unittest

from tests.unit_test_helper import is_answer




class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab19.ch019_t09_inheritance_ans import ElectricCar, my_car
        else:
            from lab.lab19.ch019_t09_inheritance import ElectricCar, my_car
        self.assertIsInstance(my_car, ElectricCar)
        self.assertEqual("new", my_car.condition)
        self.assertEqual("DeLorean", my_car.model)
        self.assertEqual("silver", my_car.color)
        self.assertEqual(88, my_car.mpg)
        self.assertEqual("molten salt", my_car.battery_type)


if __name__ == '__main__':
    unittest.main()
