import unittest

from ..console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        result = get_script_output("lab01/ch01_t01_hello_world.py")
        self.assertEqual("Hello, world!\n", result)


if __name__ == '__main__':
    unittest.main()
