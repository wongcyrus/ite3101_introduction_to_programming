import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab08/ch08_t13_remove_few_things.py")
        print(temp_locals)
        self.assertListEqual(['xylophone', 'tent', 'bread loaf'], temp_locals['backpack'])


if __name__ == '__main__':
    unittest.main()
