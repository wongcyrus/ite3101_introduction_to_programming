import unittest

from tests.unit_test_helper.console_test_helper import execfile


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab18/ch018_t09_they_are_multiplying.py")

        expected = f"""good
good
good
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
