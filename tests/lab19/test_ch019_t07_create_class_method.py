import unittest

from tests.unit_test_helper.console_test_helper import execfile


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab19/ch019_t07_create_class_method.py")

        expected = f"""This is a silver DeLorean with 88 MPG.
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
