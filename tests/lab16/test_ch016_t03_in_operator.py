import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab16/ch016_t03_in_operator.py")
        expect = {
            "Name": "Peter",
            "Age": 18,
            "BDFL": True
        }
        self.assertDictEqual(expect, temp_locals['my_dict'])
        expect_output = """dict_keys(['Name', 'Age', 'BDFL'])
dict_values(['Peter', 18, True])
Name Peter
Age 18
BDFL True
"""
        self.assertEqual(expect_output, output)


if __name__ == '__main__':
    unittest.main()
