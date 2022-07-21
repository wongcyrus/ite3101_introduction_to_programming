import unittest

from tests.unit_test_helper.console_test_helper import execfile
from tests.unit_test_helper.timeout import timeout


class TestOutput(unittest.TestCase):

    def testOutput(self):
        @timeout(1)
        def run():
            temp_globals, temp_locals, content, output = execfile("lab13/ch013_t05_infinite_loops.py")
            return output

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
        self.assertEqual(expected, run())


if __name__ == '__main__':
    unittest.main()
