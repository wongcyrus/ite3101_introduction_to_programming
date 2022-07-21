import unittest

from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab06/ch06_t08_generic_imports.py")

        self.assertEqual("5.0\n", output)
        print(content)
        print(content.count("math"))
        self.assertEqual(2, content.count("math"))
        self.assertEqual(1, content.count("import math"))


if __name__ == '__main__':
    unittest.main()
