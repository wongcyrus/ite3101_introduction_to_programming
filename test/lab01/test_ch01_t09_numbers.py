import unittest
from test.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content = execfile("lab01/ch01_t09_numbers.py")
        print(temp_locals)
        self.assertEqual(temp_locals['cucumbers'], 1)
        self.assertEqual(temp_locals['price_per_cucumber'], 3.25)
        self.assertEqual(temp_locals['total_cost'], 3.25)


if __name__ == '__main__':
    unittest.main()
