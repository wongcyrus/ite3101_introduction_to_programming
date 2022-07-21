import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab02/ch02_t04_access_by_index.py")
        print(temp_locals)
        self.assertEqual('Y', temp_locals['fifth_letter'])


if __name__ == '__main__':
    unittest.main()
