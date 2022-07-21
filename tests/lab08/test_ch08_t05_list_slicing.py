import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab08/ch08_t05_list_slicing.py")
        print(temp_locals)
        self.assertListEqual(['passport', 'laptop'], temp_locals["middle"])
        self.assertListEqual(['suit', 'shoes'], temp_locals["last"])


if __name__ == '__main__':
    unittest.main()
