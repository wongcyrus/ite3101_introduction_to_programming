import unittest

from ..console_test_helper import execfile
from ..timeout import timeout


class TestOutput(unittest.TestCase):

    @timeout(1)
    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab13/ch013_t17_for_else.py")

        expected = """You have...
A banana
A apple
A orange
A tomato is not a fruit!
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
