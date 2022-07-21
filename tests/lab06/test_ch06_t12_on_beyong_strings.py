import unittest

from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab06/ch06_t12_on_beyong_strings.py")

        self.assertEqual("""10
-10
10
""", output)


if __name__ == '__main__':
    unittest.main()
