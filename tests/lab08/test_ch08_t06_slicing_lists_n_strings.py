import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab08/ch08_t06_slicing_lists_n_strings.py")
        self.assertEqual("cat", temp_locals["cat"])
        self.assertEqual("dog", temp_locals["dog"])
        self.assertEqual("frog", temp_locals["frog"])


if __name__ == '__main__':
    unittest.main()
