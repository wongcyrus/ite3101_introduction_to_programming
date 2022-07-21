import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab05/ch05_t06_ay_b_c.py")
        print(temp_locals)
        self.assertEqual("ay", temp_locals["pyg"])


if __name__ == '__main__':
    unittest.main()
