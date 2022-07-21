import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab01/ch01_t06_arithmetic.py")
        print(temp_locals)
        self.assertIsInstance(temp_locals['product'], int)
        self.assertEqual(1, temp_locals['remainder'])


if __name__ == '__main__':
    unittest.main()
