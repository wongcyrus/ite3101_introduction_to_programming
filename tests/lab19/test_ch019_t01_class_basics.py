import unittest
from tests.unit_test_helper import is_answer




class TestOutput(unittest.TestCase):

    def setUp(self):
        if is_answer:
            from lab.lab19.ch019_t01_class_basics_ans import Car
        else:
            from lab.lab19.ch019_t01_class_basics import Car
        self.car = Car()

    def test(self):
        if is_answer:
            from lab.lab19.ch019_t01_class_basics_ans import Car
        else:
            from lab.lab19.ch019_t01_class_basics import Car
        self.assertIsInstance(self.car, Car)


if __name__ == '__main__':
    unittest.main()
