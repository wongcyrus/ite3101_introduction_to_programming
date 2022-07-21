import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab16/ch016_t18_lambda_expressions.py")
        self.assertEqual("IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX",
                         temp_locals['garbled'])
        self.assertEqual("I am another secret message!", temp_locals['message'])


if __name__ == '__main__':
    unittest.main()
