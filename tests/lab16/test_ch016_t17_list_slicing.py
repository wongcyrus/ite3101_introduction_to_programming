import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab16/ch016_t17_list_slicing.py")
        self.assertEqual("!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI", temp_locals['garbled'])
        self.assertEqual("I am the secret message!", temp_locals['message'])


if __name__ == '__main__':
    unittest.main()
