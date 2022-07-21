import unittest
from tests.unit_test_helper.console_test_helper import get_script_output

class TestOutput(unittest.TestCase):

    def test(self):
        result = get_script_output("lab01/ch01_t01_hello_world.py")
        self.assertEqual("Hello, world!\n", result)


if __name__ == '__main__':
    unittest.main()
