import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab16/ch016_t15_iterating_dict.py")
        self.assertDictEqual({
            "Monty Python and the Holy Grail": "Great",
            "Monty Python's Life of Brian": "Good",
            "Monty Python's Meaning of Life": "Okay"
        }, temp_locals['movies'])
        expect_output = """dict_items([('Monty Python and the Holy Grail', 'Great'), ("Monty Python's Life of Brian", 'Good'), ("Monty Python's Meaning of Life", 'Okay')])
"""
        self.assertEqual(expect_output, output)


if __name__ == '__main__':
    unittest.main()
