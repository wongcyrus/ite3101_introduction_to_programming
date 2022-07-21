# ch03_t01_the_datetime_library
import datetime
import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab03/ch03_t01_the_datetime_library.py")
        print(temp_locals)
        self.assertIs(temp_locals['datetime'], datetime.datetime)


if __name__ == '__main__':
    unittest.main()
