import unittest

from tests.unit_test_helper.console_test_helper import execfile
from tests.unit_test_helper.timeout import timeout


class TestOutput(unittest.TestCase):

    @timeout(1)
    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab13/ch013_t16_mul_lists.py")

        expected = """3
9
17
15
30
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
