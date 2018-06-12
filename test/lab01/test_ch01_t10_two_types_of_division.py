import unittest
from test.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content = execfile("lab01/ch01_t10_two_types_of_division.py")
        print(temp_locals)
        self.assertEqual(temp_locals['cucumbers'], 100)
        self.assertEqual(temp_locals['num_people'], 6)
        self.assertEqual(temp_locals['whole_cucumbers_per_person'], 16)
        self.assertEqual(temp_locals['float_cucumbers_per_person'], 16.666666666666668)


if __name__ == '__main__':
    unittest.main()
