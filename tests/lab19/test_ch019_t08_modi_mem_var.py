import unittest

from tests.unit_test_helper.console_test_helper import execfile


class TestOutput(unittest.TestCase):

    def test(self):
        temp_globals, temp_locals, content, output = execfile("lab19/ch019_t08_modi_mem_var.py")

        expected = f"""new
used
"""
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
