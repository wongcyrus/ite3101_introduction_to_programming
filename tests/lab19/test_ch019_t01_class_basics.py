import unittest
from ..console_test_helper import is_answer

if is_answer:
    from lab.lab19.ch019_t01_class_basics_ans import Car
else:
    from lab.lab19.ch019_t01_class_basics import Car


class TestOutput(unittest.TestCase):

    def setUp(self):
        self.car = Car()

    def test(self):
        self.assertIsInstance(self.car, Car)


if __name__ == '__main__':
    unittest.main()
