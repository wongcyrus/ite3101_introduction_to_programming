import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab16/ch016_t01_iterators_for_dict.py")
        expect = {
            "Name": "Peter",
            "Age": 18,
            "BDFL": True
        }
        self.assertDictEqual(expect, temp_locals['my_dict'])
        self.assertEqual("dict_items([('Name', 'Peter'), ('Age', 18), ('BDFL', True)])\n", output)


if __name__ == '__main__':
    unittest.main()
