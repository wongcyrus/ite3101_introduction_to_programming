import unittest
from ..console_test_helper import is_answer

if is_answer:
    from lab.lab19.ch019_t03_class_mem_var_ans import Car, my_car
else:
    from lab.lab19.ch019_t03_class_mem_var import Car, my_car


class TestOutput(unittest.TestCase):

    def test(self):
        self.assertIsInstance(my_car, Car)
        self.assertEqual("new", my_car.condition)


if __name__ == '__main__':
    unittest.main()
