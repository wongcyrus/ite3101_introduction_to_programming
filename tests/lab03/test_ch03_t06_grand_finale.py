import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab03/ch03_t06_grand_finale.py")
        print(temp_locals)

        now = temp_locals['now']

        expected = '%02d/%02d/%04d %02d:%02d:%02d' % (
            now.month, now.day, now.year, now.hour, now.minute, now.second) + "\n"
        self.assertIsNotNone(temp_locals['now'])
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
