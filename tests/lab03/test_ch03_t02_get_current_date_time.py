import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab03/ch03_t02_get_current_date_time.py")
        print(temp_locals)
        self.assertIsNotNone(temp_locals['datetime'])

    def test_output(self):
        result = get_script_output("lab03/ch03_t02_get_current_date_time.py")
        self.assertEqual(27, len(result))


if __name__ == '__main__':
    unittest.main()
