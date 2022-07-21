import unittest

from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab06/ch06_t10_universal_imports.py")

        self.assertEqual("5.0\n", output)
        print(content)
        print(content.count("math"))
        self.assertEqual(2, content.count("math"))
        self.assertEqual(1, content.count("from math import *"))


if __name__ == '__main__':
    unittest.main()
