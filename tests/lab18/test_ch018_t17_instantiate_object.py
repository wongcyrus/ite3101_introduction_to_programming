import unittest

from tests.unit_test_helper.console_test_helper import execfile


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab18/ch018_t17_instantiate_object.py")

        expected = f"""3
True
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
