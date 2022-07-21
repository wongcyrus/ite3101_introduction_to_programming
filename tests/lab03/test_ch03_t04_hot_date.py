import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab03/ch03_t04_hot_date.py")
        print(temp_locals)

        now = temp_locals['now']

        expected = '%02d/%02d/%04d' % (now.month, now.day, now.year) + "\n"
        self.assertIsNotNone(temp_locals['now'])
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
