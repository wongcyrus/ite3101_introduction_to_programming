import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test_variable(self):
        temp_globals, temp_locals, content, output = execfile("lab02/ch02_t05_string_methods.py")
        print(temp_locals)
        self.assertEqual('Norwegian Blue', temp_locals['parrot'])

    def test_output(self):
        result = get_script_output("lab02/ch02_t05_string_methods.py")
        self.assertEqual("14\n", result)


if __name__ == '__main__':
    unittest.main()
