import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab16/ch016_t06_now_u_try.py")
        self.assertListEqual([8, 64, 216, 512, 1000], temp_locals['cubes_by_four'])
        expect_output = """[8, 64, 216, 512, 1000]
"""
        self.assertEqual(expect_output, output)


if __name__ == '__main__':
    unittest.main()
