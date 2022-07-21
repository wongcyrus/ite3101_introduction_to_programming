import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab04/ch04_t06_and.py")
        print(temp_locals)

        expected = {'bool_one': False, 'bool_two': False, 'bool_three': False, 'bool_four': True, 'bool_five': True}

        self.assertDictEqual(expected, temp_locals)


if __name__ == '__main__':
    unittest.main()
