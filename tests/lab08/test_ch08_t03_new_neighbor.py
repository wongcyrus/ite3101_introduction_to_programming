import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab08/ch08_t03_new_neighbor.py")
        print(temp_locals)
        self.assertNotEqual("tiger", temp_locals["zoo_animals"][3])


if __name__ == '__main__':
    unittest.main()
