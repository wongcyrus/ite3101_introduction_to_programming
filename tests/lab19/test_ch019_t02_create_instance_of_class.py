import unittest
from tests.unit_test_helper import is_answer




class TestOutput(unittest.TestCase):

    def test(self):
        if is_answer:
            from lab.lab19.ch019_t02_create_instance_of_class_ans import Car, my_car
        else:
            from lab.lab19.ch019_t02_create_instance_of_class import Car, my_car
        self.assertIsInstance(my_car, Car)


if __name__ == '__main__':
    unittest.main()
