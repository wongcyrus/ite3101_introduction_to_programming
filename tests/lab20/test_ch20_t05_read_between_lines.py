import unittest

from tests.unit_test_helper.console_test_helper import execfile


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab20/ch20_t05_read_between_lines.py")

        expected = f"""I'm the first line of the file!

I'm the second line.

Third line here, boss.
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
