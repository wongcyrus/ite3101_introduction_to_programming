import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab03/ch03_t03_extracting_Info.py")
        print(temp_locals)

        now = temp_locals['now']

        expected = str(now) + "\n" + \
                   str(now.year) + "\n" + \
                   str(now.month) + "\n" + \
                   str(now.day) + "\n"

        self.assertIsNotNone(temp_locals['now'])
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
