import unittest

from tests.unit_test_helper.console_test_helper import execfile


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab10/ch010_t04_for_the_record.py")

        expected = """Lloyd
[90.0, 97.0, 75.0, 92.0]
[88.0, 40.0, 94.0]
[75.0, 90.0]
Alice
[100.0, 92.0, 98.0, 100.0]
[82.0, 83.0, 91.0]
[89.0, 97.0]
Tyler
[0.0, 87.0, 75.0, 22.0]
[0.0, 75.0, 78.0]
[100.0, 100.0]
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
