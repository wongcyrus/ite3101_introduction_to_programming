import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab04/ch04_t11_con_statement_syntax.py")
        print(temp_locals)
        self.assertEqual('Y', temp_locals["response"])


if __name__ == '__main__':
    unittest.main()
