import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab08/ch08_t04_late_arri_n_list_len.py")
        print(temp_locals)
        self.assertEqual(4, temp_locals["list_length"])
        self.assertListEqual(['sunglasses', 'bathing suit', 'T-shirt', 'Jacket'], temp_locals["suitcase"])


if __name__ == '__main__':
    unittest.main()
