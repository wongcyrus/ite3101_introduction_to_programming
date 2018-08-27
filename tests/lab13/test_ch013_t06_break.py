import unittest

from ..console_test_helper import execfile
from ..timeout import timeout


class TestOutput(unittest.TestCase):

    @timeout(1)
    def testOutput(self):
        temp_globals, temp_locals, content, output = execfile("lab13/ch013_t06_break.py")

        expected = """0
1
2
3
4
5
6
7
8
9
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
