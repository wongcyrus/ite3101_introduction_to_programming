import unittest
from test.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content = execfile("lab01/ch01_t13_value_error.py")
        print(temp_locals)
        self.assertEqual(temp_locals['product'], 10.0)
        self.assertEqual(temp_locals['big_string'], 'The product was 10.0')


if __name__ == '__main__':
    unittest.main()
