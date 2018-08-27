import unittest
from ..console_test_helper import is_answer

if is_answer:
    from lab.lab19.ch019_t02_create_instance_of_class_ans import Car, my_car
else:
    from lab.lab19.ch019_t02_create_instance_of_class import Car, my_car


class TestOutput(unittest.TestCase):

    def test(self):
        self.assertIsInstance(my_car, Car)


if __name__ == '__main__':
    unittest.main()
