import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab08/ch08_t14_last_note.py")
        print(temp_locals)
        expected = {'gold': 550, 'pouch': ['flint', 'gemstone', 'twine'],
                    'backpack': ['bedroll', 'bread loaf', 'xylophone'],
                    'burlap bag': ['apple', 'small ruby', 'three-toed sloth'],
                    'pocket': ['seashell', 'strange berry', 'lint']}
        self.assertDictEqual(expected, temp_locals['inventory'])


if __name__ == '__main__':
    unittest.main()
