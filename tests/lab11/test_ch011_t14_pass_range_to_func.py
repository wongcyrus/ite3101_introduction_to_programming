import unittest

from tests.unit_test_helper.console_test_helper import execfile


class TestOutput(unittest.TestCase):

    def testOutput(self):
        temp_globals, temp_locals, content, output = execfile("lab11/ch011_t14_pass_range_to_func.py")

        expected = """[0, 1, 2]
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
