import unittest

from tests.unit_test_helper.console_test_helper import execfile


class TestOutput(unittest.TestCase):

    def testOutput(self):
        temp_globals, temp_locals, content, output = execfile("lab11/ch011_t12_print_list_item_by_item_in_func.py")

        expected = """3
5
7
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
