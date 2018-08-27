import unittest

from ..console_test_helper import execfile
from ..timeout import timeout


class TestOutput(unittest.TestCase):

    @timeout(1)
    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab13/ch013_t12_for_yr_A.py")

        expected = """X bird in the hXnd...
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
