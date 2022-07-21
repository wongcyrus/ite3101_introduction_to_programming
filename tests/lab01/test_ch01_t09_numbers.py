import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab01/ch01_t09_numbers.py")
        print(temp_locals)
        self.assertEqual(1, temp_locals['cucumbers'])
        self.assertEqual(3.25, temp_locals['price_per_cucumber'])
        self.assertEqual(3.25, temp_locals['total_cost'])


if __name__ == '__main__':
    unittest.main()
