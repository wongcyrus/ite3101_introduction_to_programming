import unittest
from tests.unit_test_helper.console_test_helper import *
import datetime


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab01/ch01_t05_variables.py")
        print(temp_locals)
        self.assertEqual(temp_locals['todays_date'], f"{datetime.datetime.now():%d/%m/%Y}")


if __name__ == '__main__':
    unittest.main()
