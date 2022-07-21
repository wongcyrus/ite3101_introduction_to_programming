import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab04/ch04_t09_this_n_that.py")
        print(temp_locals)

        expected = {'bool_one': False, 'bool_two': True, 'bool_three': True, 'bool_four': True, 'bool_five': False}

        self.assertDictEqual(expected, temp_locals)


if __name__ == '__main__':
    unittest.main()
