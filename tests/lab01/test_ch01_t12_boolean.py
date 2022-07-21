import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab01/ch01_t12_boolean.py")
        print(temp_locals)
        self.assertFalse(temp_locals['age_is_12'])
        self.assertTrue(temp_locals['name_is_maria'])


if __name__ == '__main__':
    unittest.main()
