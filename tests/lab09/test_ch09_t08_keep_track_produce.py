import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab09/ch09_t08_keep_track_produce.py")

        expected = """banana
price: 4
stock: 6
apple
price: 2
stock: 0
orange
price: 1.5
stock: 32
pear
price: 3
stock: 15
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
