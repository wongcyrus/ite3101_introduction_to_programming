import unittest

from tests.unit_test_helper.console_test_helper import execfile


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab20/ch20_t04_reading.py")

        expected = f"""1
4
9
16
25
36
49
64
81
100

"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
