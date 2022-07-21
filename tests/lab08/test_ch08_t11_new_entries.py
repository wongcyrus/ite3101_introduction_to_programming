import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab08/ch08_t11_new_entries.py")
        print(temp_locals)
        self.assertGreaterEqual(len(temp_locals['menu']), 4)


if __name__ == '__main__':
    unittest.main()
