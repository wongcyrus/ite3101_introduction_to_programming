import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab01/ch01_t10_two_types_of_division.py")
        print(temp_locals)
        self.assertEqual(100, temp_locals['cucumbers'])
        self.assertEqual(6, temp_locals['num_people'])
        self.assertEqual(16, temp_locals['whole_cucumbers_per_person'])
        self.assertEqual(16.666666666666668, temp_locals['float_cucumbers_per_person'])


if __name__ == '__main__':
    unittest.main()
