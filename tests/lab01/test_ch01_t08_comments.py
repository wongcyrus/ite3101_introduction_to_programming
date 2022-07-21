import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab01/ch01_t08_comments.py")
        print(content)
        self.assertTrue("#" in content)


if __name__ == '__main__':
    unittest.main()
