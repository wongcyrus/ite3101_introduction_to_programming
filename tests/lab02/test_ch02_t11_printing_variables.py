import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test_variable(self):
        temp_globals, temp_locals, content, output = execfile("lab02/ch02_t11_printing_variables.py")
        print(temp_locals)
        self.assertEqual('Ping!', temp_locals['the_machine_goes'])

    def test_output(self):
        result = get_script_output("lab02/ch02_t11_printing_variables.py")
        self.assertEqual("Ping!\n", result)


if __name__ == '__main__':
    unittest.main()
