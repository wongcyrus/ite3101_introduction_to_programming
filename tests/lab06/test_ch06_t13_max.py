import unittest

from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab06/ch06_t13_max.py")

        self.assertEqual("""12.1
""", output)


if __name__ == '__main__':
    unittest.main()
