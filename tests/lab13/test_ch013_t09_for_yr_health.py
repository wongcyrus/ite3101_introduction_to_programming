import unittest

from tests.unit_test_helper.console_test_helper import execfile
from tests.unit_test_helper.timeout import timeout


class TestOutput(unittest.TestCase):

    @timeout(1)
    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab13/ch013_t09_for_yr_health.py")

        expected = """Counting...
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
