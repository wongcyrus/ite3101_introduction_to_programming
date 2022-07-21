import unittest
from tests.unit_test_helper.console_test_helper import *


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab08/ch08_t12_change_yr_mind.py")
        print(temp_locals)
        self.assertEqual(2, len(temp_locals['zoo_animals']))
        self.assertNotIn('Sloth', temp_locals['zoo_animals'])
        self.assertNotIn('Bengal Tiger', temp_locals['zoo_animals'])
        self.assertNotEqual('Arctic Exhibit', temp_locals['zoo_animals']['Rockhopper Penguin'])


if __name__ == '__main__':
    unittest.main()
