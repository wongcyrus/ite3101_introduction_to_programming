import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab01/ch01_t13_value_error.py")
        print(temp_locals)
        self.assertEqual(10.0, temp_locals['product'])
        self.assertEqual('The product was 10.0', temp_locals['big_string'])


if __name__ == '__main__':
    unittest.main()
