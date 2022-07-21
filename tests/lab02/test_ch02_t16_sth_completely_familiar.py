import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test_output(self):
        temp_globals, temp_locals, content, output = execfile("lab02/ch02_t16_sth_completely_familiar.py")
        print(temp_locals)
        value = str(temp_locals['my_string'])
        length = len(value)
        expect = f"""{length}
{value.upper()}
"""
        self.assertEqual(expect, output)


if __name__ == '__main__':
    unittest.main()
