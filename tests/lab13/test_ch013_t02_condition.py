import unittest

from ..console_test_helper import execfile
from ..timeout import timeout


class TestOutput(unittest.TestCase):

    @timeout(1)
    def testOutput(self):
        temp_globals, temp_locals, content, output = execfile("lab13/ch013_t02_condition.py")

        expected = """I am a loop
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
