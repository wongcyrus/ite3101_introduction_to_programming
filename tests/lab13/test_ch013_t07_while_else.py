import unittest
from unittest.mock import patch

from tests.unit_test_helper.console_test_helper import execfile
from tests.unit_test_helper.timeout import timeout


class TestOutput(unittest.TestCase):

    @timeout(1)
    @patch("random.randint", lambda x, y: 1)
    def test_all_one(self):
        temp_globals, temp_locals, content, output = execfile("lab13/ch013_t07_while_else.py")

        expected = """Lucky Numbers! 3 numbers will be generated.
If one of them is a '5', you lose!
1
1
1
You win!
"""
        self.assertEqual(expected, output)

    @timeout(1)
    @patch("random.randint", lambda x, y: 5)
    def test_five(self):
        temp_globals, temp_locals, content, output = execfile("lab13/ch013_t07_while_else.py")

        expected = """Lucky Numbers! 3 numbers will be generated.
If one of them is a '5', you lose!
5
Sorry, you lose!
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
