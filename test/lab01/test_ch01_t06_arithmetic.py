import unittest
from test.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content = execfile("lab01/ch01_t06_arithmetic.py")
        print(temp_locals)
        self.assertIsInstance(temp_locals['product'], int)
        self.assertEqual(temp_locals['remainder'], 1)


if __name__ == '__main__':
    unittest.main()
