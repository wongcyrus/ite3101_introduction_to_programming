import unittest

from tests.unit_test_helper.console_test_helper import execfile


class TestOutput(unittest.TestCase):

    def testOutput(self):
        temp_globals, temp_locals, content, output = execfile("lab11/ch011_t01_list_accessing.py")

        expected = """3
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
