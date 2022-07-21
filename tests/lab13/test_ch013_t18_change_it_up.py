import unittest

from tests.unit_test_helper.console_test_helper import execfile
from tests.unit_test_helper.timeout import timeout


class TestOutput(unittest.TestCase):

    @timeout(1)
    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab13/ch013_t18_change_it_up.py")

        expected = """You have...
A banana
A apple
A orange
A tomato is not a fruit!
A tomato
A pear
A grape
A fine selection of fruits!
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
