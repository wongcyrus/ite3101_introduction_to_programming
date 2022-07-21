import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab08/ch08_t07_maintaining_order.py")
        print(temp_locals)
        self.assertListEqual(['aardvark', 'badger', 'cobra', 'duck', 'emu', 'fennec fox'], temp_locals["animals"])
        self.assertEqual(2, temp_locals["duck_index"])


if __name__ == '__main__':
    unittest.main()
