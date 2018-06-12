import unittest
from test.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content = execfile("lab02/ch02_t02_practice.py")
        print(temp_locals)
        self.assertEqual(temp_locals['caesar'], 'Graham')
        self.assertEqual(temp_locals['praline'], 'John')
        self.assertEqual(temp_locals['viking'], 'Teresa')


if __name__ == '__main__':
    unittest.main()
