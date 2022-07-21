import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab02/ch02_t03_escaping_characters.py")
        print(temp_locals)
        self.assertEqual("This isn't flying, this is falling with style!", temp_locals['__doc__'])


if __name__ == '__main__':
    unittest.main()
