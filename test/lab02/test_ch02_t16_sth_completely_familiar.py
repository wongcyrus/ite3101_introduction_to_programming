import unittest
from test.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test_variable(self):
        temp_globals, temp_locals, content = execfile("lab02/ch02_t16_sth_completely_familiar.py")
        print(temp_locals)
        self.assertEqual('Hello', temp_locals['my_string'])

    def test_output(self):
        result = get_script_output("lab02/ch02_t16_sth_completely_familiar.py")
        self.assertEqual('5\nHELLO\n', result)


if __name__ == '__main__':
    unittest.main()
