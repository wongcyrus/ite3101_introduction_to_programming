import unittest

from tests.unit_test_helper.console_test_helper import execfile
from tests.unit_test_helper.timeout import timeout


class TestOutput(unittest.TestCase):

    @timeout(1)
    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab13/ch013_t19_create_yr_own.py")

        expected = """0
1
2
End
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
