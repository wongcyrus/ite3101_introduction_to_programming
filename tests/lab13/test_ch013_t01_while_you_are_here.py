import unittest

from tests.unit_test_helper.console_test_helper import execfile
from tests.unit_test_helper.timeout import timeout


class TestOutput(unittest.TestCase):

    @timeout(1)
    def testOutput(self):
        temp_globals, temp_locals, content, output = execfile("lab13/ch013_t01_while_you_are_here.py")

        expected = """Hello, I am an if statement and count is 0
Hello, I am a while and count is 0
Hello, I am a while and count is 1
Hello, I am a while and count is 2
Hello, I am a while and count is 3
Hello, I am a while and count is 4
Hello, I am a while and count is 5
Hello, I am a while and count is 6
Hello, I am a while and count is 7
Hello, I am a while and count is 8
Hello, I am a while and count is 9
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
