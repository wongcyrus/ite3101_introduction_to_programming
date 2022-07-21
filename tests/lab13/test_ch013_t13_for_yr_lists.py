import unittest

from tests.unit_test_helper.console_test_helper import execfile
from tests.unit_test_helper.timeout import timeout


class TestOutput(unittest.TestCase):

    @timeout(1)
    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab13/ch013_t13_for_yr_lists.py")

        expected = """This list contains: 
7
9
12
54
99
49
81
144
2916
9801
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
