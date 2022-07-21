import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab02/ch02_t02_practice.py")
        print(temp_locals)
        self.assertEqual('Graham', temp_locals['caesar'])
        self.assertEqual('John', temp_locals['praline'])
        self.assertEqual('Teresa', temp_locals['viking'])


if __name__ == '__main__':
    unittest.main()
