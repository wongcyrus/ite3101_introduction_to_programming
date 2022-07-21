import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab16/ch016_t13_lambda_syntax.py")
        self.assertListEqual(["HTML", "JavaScript", "Python", "Ruby"], temp_locals['languages'])
        expect_output = """['Python']
"""
        self.assertEqual(expect_output, output)


if __name__ == '__main__':
    unittest.main()
